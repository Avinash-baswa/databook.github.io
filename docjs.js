const start = document.querySelector('button');
var ta = document.getElementById('ocr');
document.getElementById('ip_file').addEventListener('change', function() {

  var file = this.files[0];
  if (file) {
    var reader = new FileReader();
    reader.onload = function(e) {
      document.getElementById('pro').src = e.target.result;
       document.getElementById('pro').style.display = 'block';

 ta.innerHTML = ''
    const rec = new Tesseract.TesseractWorker()
    rec.recognize(e.target.result)
        .progress(function (response) {
            if(response.status == 'recognizing text'){
                ta.innerHTML = response.status + '   ' + response.progress
            }else{
                ta.innerHTML = response.status
            }
        })
        .then(function (data) {
            ta.innerHTML = data.text

        })








    };
    reader.readAsDataURL(file);
  }
});



// now start text recognition
//start.onclick = () => {
//    ta.innerHTML = ''
//    const rec = new Tesseract.TesseractWorker()
//    rec.recognize(fileSelector.files[0])
//        .progress(function (response) {
//            if(response.status == 'recognizing text'){
//                progress.innerHTML = response.status + '   ' + response.progress
//            }else{
//                progress.innerHTML = response.status
//            }
//        })
//        .then(function (data) {
//            textarea.innerHTML = data.text
//            progress.innerHTML = 'Done'
//        })
//}