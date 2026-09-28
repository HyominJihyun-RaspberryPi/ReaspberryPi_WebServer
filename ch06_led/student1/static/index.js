const led = document.getElementById("led");
const on = document.getElementById("on");
const off = document.getElementById("off");

const ledArea = document.getElementById("ledArea");
const status = document.getElementById("status");

// ON 버튼
on.addEventListener("click", function () {
fetch("/on", { method: "POST" })
.then(response => {
if (!response.ok) {
throw new Error("HTTP error " + response.status);
}


        led.src = "/static/on.png";

        on.classList.add("active");
        off.classList.remove("active");

        ledArea.classList.add("on");
        status.classList.add("on");

        status.innerHTML =
            '<span class="status-dot"></span> LED ON';
    })
    .catch(error => {
        alert(error);
    });

});

// OFF 버튼
off.addEventListener("click", function () {
fetch("/off", { method: "POST" })
.then(response => {
if (!response.ok) {
throw new Error("HTTP error " + response.status);
}

        led.src = "/static/off.png";

        off.classList.add("active");
        on.classList.remove("active");

        ledArea.classList.remove("on");
        status.classList.remove("on");

        status.innerHTML =
            '<span class="status-dot"></span> LED OFF';
    })
    .catch(error => {
        alert(error);
    });


});

