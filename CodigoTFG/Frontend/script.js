// Guardamos el último texto para poder enviar feedback después
let ultimoTexto = "";

// Función principal que se ejecuta al pulsar "Analizar"
async function analizarTexto() {

    // Obtenemos el texto del usuario
    const texto = document.getElementById("texto").value;

    // Comprobamos que no esté vacío
    if (texto.trim() === "") {
        alert("Por favor, escribe algún texto.");
        return;
    }

    // Guardamos el texto para usarlo después en feedback
    ultimoTexto = texto;

    try {
        // Enviamos petición al endpoint /predict
        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                texto: texto
            })
        });

        // Convertimos la respuesta a JSON
        const data = await response.json();

        // Barra de riesgo (0 a 100%)
        const barra = document.getElementById("barra-riesgo");

        // Reiniciamos la barra para evitar errores visuales en múltiples usos
        barra.style.width = "0%";
        barra.style.backgroundColor = "green";

        // Asignamos porcentaje según el riesgo
        let porcentaje = 0;

        if (data.riesgo === "bajo") {
            porcentaje = 30;
            barra.style.backgroundColor = "green";
        } else if (data.riesgo === "medio") {
            porcentaje = 60;
            barra.style.backgroundColor = "orange";
        } else if (data.riesgo === "alto") {
            porcentaje = 90;
            barra.style.backgroundColor = "red";
        }

        // Aplicamos el tamaño a la barra
        barra.style.width = porcentaje + "%";

        // Mostramos el riesgo
        const riesgoElemento = document.getElementById("riesgo");
        riesgoElemento.innerText = "Nivel de riesgo: " + data.riesgo;

        // Quitamos clases anteriores
        riesgoElemento.classList.remove("bajo", "medio", "alto");

        // Añadimos color según el riesgo
        if (data.riesgo === "bajo") {
            riesgoElemento.classList.add("bajo");
        } else if (data.riesgo === "medio") {
            riesgoElemento.classList.add("medio");
        } else if (data.riesgo === "alto") {
            riesgoElemento.classList.add("alto");
        }

        // Mostramos la confianza
        document.getElementById("confianza").innerText =
            "Confianza: " + data.confianza;

        // Mostramos las secciones ocultas
        document.getElementById("resultado").classList.remove("hidden");
        document.getElementById("feedback").classList.remove("hidden");

    } catch (error) {
        console.error("Error:", error);
        alert("Error al conectar con la API");
    }
}


// Función para enviar feedback del usuario
async function enviarFeedback(feedback) {

    try {
        // Enviamos feedback al endpoint /feedback
        await fetch("http://127.0.0.1:8000/feedback", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                texto: ultimoTexto,
                feedback: feedback
            })
        });

        alert("Gracias por tu feedback");

    } catch (error) {
        console.error("Error:", error);
    }
}