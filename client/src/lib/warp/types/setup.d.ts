export interface Parameter {
  key: number,
  valueLength: number,
  value: number
}
export interface PayloadClient {
  numberOfSupportedVersions: number,
  supportedVersion: number[],
  parameters: SETUPParameter[]
}
export interface PayloadServer {
  selectedVersion: number,
  parameters: Parameter[]
}
