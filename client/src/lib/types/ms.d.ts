declare module 'MediaStreamTrackGenerator';

interface MediaStreamTrackGenerator extends MediaStreamTrack {
  writable: WritableStream;
}

declare const MediaStreamTrackGenerator: {
  prototype: MediaStreamTrackGenerator;
  new({ kind: string }): MediaStreamTrackGenerator;
};
