function courses_vald() {
    var course1 = document.getElementById("validationDefault10");
    var course2 = document.getElementById("validationDefault11");
    var course3 = document.getElementById("validationDefault12");

    var selectedValue1 = course1.options[course1.selectedIndex].value;
    var selectedValue2 = course2.options[course2.selectedIndex].value;
    var selectedValue3 = course3.options[course3.selectedIndex].value;

    if (selectedValue1 == selectedValue2 || selectedValue2 == selectedValue3 || selectedValue1 == selectedValue3) {
        if (selectedValue1 == "Choose..." && selectedValue2 == "Choose..." && selectedValue3 == "Choose...") { //havent select any
            alert("You must choose a course to register");
        } else {
            alert("ERROR you can not select a course twice");
        }
    } else {
        alert("Student registered successfully");
        location.reload();
    }
}

function testConfirmDialog() {
    var result = confirm('Are you sure you want to delete ');
    if (result) {
        alert(username + " deleted succefully");
        location.reload();
    }
}