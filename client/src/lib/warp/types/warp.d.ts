export interface Message {
  type: number,
  length: number,
  payload: Uint8Array
}
