import { useState } from "react";


export default function chatbox(){
    const [message, setmessage] = useState("");
    const [response, setresponse] = useState("");


    async function handleSend() {
    const res = await fetch("api/textmodal", {
        method: "POST",
        body: JSON.stringify({ message }),
        headers: {"Content-Type":"application/json"}

    });
    
    const data = await res.json();
    setresponse(data.reply || data.function_result);    
}

    return(
        <div>
            <textarea value={message} onChange={(e)=> setmessage(e.target.value)} />
            <button onClick={handleSend}>Send</button>
            <div>AI: {response}</div>
        </div>
    );



}