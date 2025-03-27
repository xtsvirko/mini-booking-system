document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("booking-form");
  const resultDiv = document.getElementById("booking-result");

  if (!form) return;

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const formData = new FormData(form);

    fetch(form.action, {
      method: "POST",
      headers: {
        "X-Requested-With": "XMLHttpRequest"
      },
      body: formData,
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        form.style.display = "none";

        resultDiv.innerHTML = `
          <div class="alert alert-success" role="alert">
            <p>${data.message}</p>
            <a href="${form.dataset.redirect}" class="btn btn-success mt-2">
              View My Bookings
            </a>
          </div>
        `;
      } else {
        resultDiv.innerHTML = `
          <div class="alert alert-danger" role="alert">
            ${data.error || "Something went wrong."}
          </div>
        `;
      }
    })
    .catch(err => {
      resultDiv.innerHTML = `
        <div class="alert alert-danger" role="alert">
          Server error. Please try again later.
        </div>
      `;
      console.error("AJAX error:", err);
    });
  });
});
