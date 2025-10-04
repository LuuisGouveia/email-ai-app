document.getElementById('emailForm').addEventListener('submit', async (e)=>{
    e.preventDefault()

    const text = document.getElementById('textInput').value
    const file = document.getElementById('fileInput').files[0];

    const formData = new FormData();
    if (text) formData.append("text", text);
    if (file) formData.append("file", file);

    const res = await fetch("https://ai-email-process.onrender.com", {
        method: "POST",
        body: formData
    });
    console.log("Essa é a resposta:",res);

    const data = await res.json();
    console.log("Esse é o data json: ", data);
    document.getElementById("categoria").textContent = data.categoria || "Erro";
    document.getElementById("resposta").textContent = data.resposta || "Não gerada";

    document.getElementById("results").classList.remove("hidden");

})