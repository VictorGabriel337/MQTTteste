const baseURL = "https://mqttteste.onrender.com"; // substitua por sua URL real do Render

function ligarLed() {
    fetch(`${baseURL}/ligar`, {
        method: "POST"
    })
    .then(response => response.text())
    .then(data => {
        console.log("Resposta do servidor:", data);
        document.getElementById("status").innerText = "LED Ligado";
    })
    .catch(error => {
        console.error("Erro ao ligar o LED:", error);
    });
}

function desligarLed() {
    fetch(`${baseURL}/desligar`, {
        method: "POST"
    })
    .then(response => response.text())
    .then(data => {
        console.log("Resposta do servidor:", data);
        document.getElementById("status").innerText = "LED Desligado";
    })
    .catch(error => {
        console.error("Erro ao desligar o LED:", error);
    });
}
