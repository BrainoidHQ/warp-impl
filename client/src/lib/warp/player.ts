export class Player {
  private mediaSource: MediaSource;
  private videoEl: HTMLMediaElement;
  private videoTrack: MediaStreamTrack;
  private audioTrack: MediaStreamTrack;
  private segments;
  constructor(videoEl: HTMLVideoElement) {
    this.mediaSource = new MediaSource();
    this.videoEl = videoEl;
    this.videoEl.src = URL.createObjectURL(this.mediaSource);
    this.segments = [];
    this.videoTrack = new MediaStreamTrackGenerator({ kind: 'video' });
    this.audioTrack = new MediaStreamTrackGenerator({ kind: 'audio' });
  }
};
