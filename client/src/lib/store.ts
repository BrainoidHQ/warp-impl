import { writable } from 'svelte/store';
import type { Writable } from 'svelte/store';

export const receivedStore: Writable<string[]> = writable([]);
