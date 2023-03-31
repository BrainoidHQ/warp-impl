import { receivedStore, ObjectListStore } from './store';

export class WT {
  private wt: WebTransport;
  private store: ObjectListStore<string>;
  private datagram: { reader: ReadableStreamDefaultReader, writer: WritableStreamDefaultWriter };
  private bidirectionalStream: { reader: ReadableStreamDefaultReader, writer: WritableStreamDefaultWriter };
  private static Encoder = new TextEncoder();
  private static Decoder = new TextDecoder();
  constructor(url: string) {
    this.wt = new WebTransport(url);
    this.datagram = this.bidirectionalStream = { reader: null, writer: null };
    this.store = new ObjectListStore(receivedStore);
  }
  async setup() {
    await this.wt.ready;
  }
  close() {
    this.wt.close();
  }
  setupDatagram() {
    this.datagram = {
      writer: this.wt.datagrams.writable.getWriter(),
      reader: this.wt.datagrams.readable.getReader()
    };
  };
  writeDatagram(message: string) {
    if (!this.wt.ready) throw new Error('WebTransport not yet ready');
    const bin = WT.Encoder.encode(message);
    this.datagram.writer.write(bin);
  }
  async readDatagram() {
    while (true) {
      const { value, done } = await this.datagram.reader.read();
      if (done) break;
      this.store.push(WT.Decoder.decode(value));
    }
  }
  async setupBidirectionalStream() {
    const bidirectionalStream = await this.wt.createBidirectionalStream();
    this.bidirectionalStream = {
      writer: bidirectionalStream.writable.getWriter(),
      reader: bidirectionalStream.readable.getReader()
    };
  }
  writeBidirectionalStream(message: string) {
    if (!this.wt.ready) throw new Error('WebTransport not yet ready');
    if (!this.bidirectionalStream.writer) throw new Error('Bidirectional Stream Writer does not exist');
    const bin = WT.Encoder.encode(message);
    this.bidirectionalStream.writer.write(bin);
  }
  async readBidirectionalStream() {
    if (!this.bidirectionalStream.reader) throw new Error('Bidirectional Stream Reader does not exist');
    while (true) {
      console.log('Receiving');
      const { value, done } = await this.bidirectionalStream.reader.read();
      if (done) break;
      this.store.push(WT.Decoder.decode(value));
    }
  }
  async writeUnidirectionalStream(message: string) {
    const unidirectionalStream = await this.wt.createUnidirectionalStream();
    const writer = unidirectionalStream.getWriter();
    const bin = WT.Encoder.encode(message);
    writer.write(bin);
  }
  async readUnidirectionalStream(callback) {
    const readerIncoming = await this.wt.incomingUnidirectionalStreams.getReader();
    while (true) {
      const { value, done } = await readerIncoming.read();
      if (done) break;
      await this.readReceiveStream(value, callback);
    }
  }
  private async readReceiveStream(stream, callback: (val: Uint8Array) => unknown) {
    const reader = stream.getReader();
    while (true) {
      const { value, done } = await reader.read();
      if (done) break;
      this.store.push(WT.Decoder.decode(value));
      callback(value);
    }
  }
}
