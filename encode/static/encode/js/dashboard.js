function appendDownload(id){
  document.getElementById(id).className = '';

}
function updateDate(){
  if (document.getElementById('date')=='0' || document.getElementById('date')==0){
    return 0;
  }
  a = document.getElementById('date').value.split('-');
  a.forEach((item, index, arr) => {arr[index] = parseInt(item);})
  return a;
}
function attendance(e){
    date = updateDate()
    var data = JSON.stringify({"option":document.getElementById('option').value,"date":date, "month":1});

    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", function() {
      if(this.readyState === 4) {
        console.log(this.responseText);
      }
    });

    xhr.open("POST", `http://127.0.0.1:8000/r/api/make_sheet/${e.dataset.classname}/`);

    xhr.send(data);
    window.setTimeout(appendDownload(e.dataset.classname) ,3000);
}
 var classes = document.querySelectorAll('.progress-bar')
 classes.forEach((classset) => {
   classset.style.width = String(classset.dataset.valuenow*100/classset.dataset.valuemax) + '%';
 })
