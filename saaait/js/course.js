async function get_course() {
    let response = await fetch("http://localhost:8000/api/course/all");
    if (response.ok) {
        let json = await response.json();
        return json;
    } else {
        alert("Ошибка HTTP: " + response.status);
    }
}

async function render_course() {
    let template = `
    <div class="card mb-3" style="max-width: 540px;">
  <div class="row g-0">
    <div class="col-md-4">
      <img src="{КАРТИНКА}" class="img-fluid rounded-start" alt="Photo" ">
    </div>
    <div class="col-md-8">
      <div class="card-body">
        <h5 class="card-title">{ГОРОД}</h5>
        <p class="card-text">{ПОГОДА}</p>
        <p class="card-text"><small class="text-body-secondary">{ПОСЛЕДНЕЕОБНОВЛЕНИЕ}</small></p>
        <a href="https://t.me/+K8iFgPuK7wdmNzBi"><button class="buy">{price}</button></a>
      </div>
    </div>
  </div>
</div>`;

    let course = await get_course();
    let container = document.getElementById("course");
    course.forEach(element => {
        let course = template
            .replace("{ГОРОД}", element.name)
            .replace("{ПОГОДА}", element.description)
            .replace("{КАРТИНКА}", element.photo)
            .replace("{ПОСЛЕДНЕЕОБНОВЛЕНИЕ}", element.DCF)
            .replace("{price}", element.buy)
        container.innerHTML += course;
    });
}

render_course();