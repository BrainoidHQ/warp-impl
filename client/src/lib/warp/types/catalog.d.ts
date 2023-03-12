interface CATALOGTrackDescriptors {
  trackID: number,
  containerFormat: number,
  containerInitPayload: Uint8Array
}

export interface CATALOG {
  broadcastURI: string,
  trackCount: number,
  trackDescriptors: CATALOGTrackDescriptors
}
