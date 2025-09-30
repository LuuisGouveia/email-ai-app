document.getElementById('emailForm').addEventListener('submit', async (e)=>{
    e.preventDefault()

    const text = document.getElementById('textInput').value
    const file = document.getElementById('fileInput').files[0];

    const formData = new FormData();
    if (text) formData.append("text", text);
    if (file) formData.append("file", file);

    const res = await fetch("http://localhost:8000/process-email", {
        method: "POST",
        body: formData
    });

    const data = await res.json();
    document.getElementById("categoria").textContent = data.categoria || "Erro";
    document.getElementById("resposta").textContent = data.resposta || "Não gerada";

    document.getElementById("results").classList.remove("hidden");

})