import { writable } from 'svelte/store';
import type { Writable } from 'svelte/store';

export const receivedStore: Writable<string[]> = writable([]);

export class ObjectListStore<StoreType> {
  public store: Writable<StoreType[]>;
  constructor(storeType: Writable<StoreType[]>) {
    this.store = storeType;
  }
  public push(data: StoreType): void {
    this.store.update((value) => {
      value.push(data);
      return value;
    });
  }
};
