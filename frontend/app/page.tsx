"use client";

import { useState, useRef } from "react";

export default function Page() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState<any>(null);
  const audioRef = useRef<HTMLAudioElement>(null);

  const handleSend = async () => {
    if (!input.trim()) return;

    try {
      const res = await fetch("http://127.0.0.1:8000/api/textmodal/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input }),
      });

      const data = await res.json();
      console.log("✅ API response:", data);
      setResponse(data);

      // Play audio if available
      if (data.function_result?.file_path && audioRef.current) {
        audioRef.current.src = data.function_result.file_path;
        audioRef.current.play();
      }

      setInput("");
    } catch (err) {
      console.error("❌ Error:", err);
    }
  };

  return (
    <main className="min-h-screen bg-black text-white flex flex-col items-center justify-center p-6 space-y-6">
      <h1 className="text-3xl font-bold text-teal-400">🎶 AI Music Assistant</h1>

      {/* Input */}
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") handleSend();
        }}
        placeholder="Type your message..."
        className="w-full max-w-md p-3 rounded bg-gray-800 text-white"
      />

      {/* Submit Button */}
      <button
        onClick={handleSend}
        className="bg-teal-500 hover:bg-teal-600 text-white px-4 py-2 rounded"
      >
        Send
      </button>

      {/* Bot Response Box */}
      {response && (
        <div className="bg-gray-900 p-4 rounded w-full max-w-md space-y-4 mt-4">

         {/* Text Message */}
{(response.reply || response.message) && (
  <div>
    <strong>🤖 Message:</strong>
    <div className="mt-2 space-y-1">
      {(response.reply || response.message).split("\n").map((line: string, idx: number) => (
        <p key={idx}>{line}</p>
      ))}
    </div>
  </div>
)}


          {/* Song Info */}
          {response.function_result && (
            <>
              {response.function_result.title && (
                <p><strong>🎵 Title:</strong> {response.function_result.title}</p>
              )}
              {response.function_result.artist && (
                <p><strong>🎤 Artist:</strong> {response.function_result.artist}</p>
              )}
              {response.function_result.file_path && (
                <audio ref={audioRef} controls className="w-full">
                  <source src={response.function_result.file_path} type="audio/mpeg" />
                  Your browser does not support the audio element.
                </audio>
              )}
            </>
          )}

          {/* Raw Debug Output */}
          <pre className="text-sm text-green-400 whitespace-pre-wrap break-words">
            {JSON.stringify(response, null, 2)}
          </pre>
        </div>
      )}
    </main>
  );
}
