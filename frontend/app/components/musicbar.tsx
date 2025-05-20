export default function MusicBar({ uri }: { uri: string }) {
  return (
    <iframe
      src={`https://open.spotify.com/embed/track/${uri}`}
      width="300"
      height="80"
      frameBorder="0"
      allow="encrypted-media"
    />
  );
}
