import { receivedStore } from './store';

export class WT {
  private wt;
  private datagram: { reader, writer };
  private static Encoder = new TextEncoder();
  private static Decoder = new TextDecoder();
  constructor(url: string) {
    this.wt = new WebTransport(url);
    this.datagram = { reader: null, writer: null };
  }
  async setup() {
    await this.wt.ready;
    this.datagram.writer = this.wt.datagrams.writable.getWriter();
    this.datagram.reader = this.wt.datagrams.readable.getReader();
  }
  writeDatagram(message: string) {
    if (!this.wt.ready) throw new Error('WebTransport not yet ready');
    const bin = WT.Encoder.encode(message);
    this.datagram.writer.write(bin);
  }
  async readDatagram() {
    while (true) {
      const { value, done } = await this.datagram.reader.read();
      if (done) break;
      receivedStore.update((val) => {
        val.push(WT.Decoder.decode(value));
        return val;
      });
    }
  }
}
