// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
declare global {
  namespace App {}
  class WebTransport {
    ready: Promise<boolean>;
    constructor(url: string)
  }
}

export {};
