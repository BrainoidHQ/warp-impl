import { WT } from '$lib/wt';

// TODO: Stick to the spec when it becomes a RFC
export class Warp {
  wt: WT;
  constructor() {
    this.wt = new WT('https://0.0.0.0:4433/counter');
  }
  async init() {
    await this.wt.setup();
    this.wt.writeUnidirectionalStream('Hello');
  }
}
