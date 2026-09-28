document.addEventListener("DOMContentLoaded", function () {
    const led = document.getElementById("led");
    const on = document.getElementById("on");
    const off = document.getElementById("off");

    // ON 버튼 클릭 이벤트
    if (on) {
        on.addEventListener("click", function () {
            fetch("/on", { method: "POST" })
                .then(response => {
                    if (!response.ok) {
                        throw new Error("HTTP error " + response.status);
                    }
                    led.src = "/static/on.png";
                })
                .catch(error => {
                    alert("Error: " + error.message);
                });
        });
    }

    // OFF 버튼 클릭 이벤트
    if (off) {
        off.addEventListener("click", function () {
            fetch("/off", { method: "POST" })
                .then(response => {
                    if (!response.ok) {
                        throw new Error("HTTP error " + response.status);
                    }
                    led.src = "/static/off.png";
                })
                .catch(error => {
                    alert("Error: " + error.message);
                });
        });
    }

    // ⌨️ 키보드 단축키 (O: ON, F: OFF)
    document.addEventListener("keydown", function (event) {
        // 대소문자 구분 없이 처리 (key 값 비교)
        const key = event.key.toLowerCase();
        
        if (key === 'o') {
            on.click(); // ON 버튼 클릭 효과 및 이벤트 실행
        } else if (key === 'f') {
            off.click(); // OFF 버튼 클릭 효과 및 이벤트 실행
        }
    });
});
