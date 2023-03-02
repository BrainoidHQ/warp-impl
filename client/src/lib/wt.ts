export class WT {
  private instance;
  private writer;
  constructor(url: string) {
    const quic = new WebTransport(url);
    this.instance = quic.ready.then(() => quic);
  }
}
