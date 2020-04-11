/*
filedrag.js - HTML5 File Drag & Drop demonstration
Featured on SitePoint.com
Developed by Craig Buckler (@craigbuckler) of OptimalWorks.net
Modified by Leon(i@leons.im)
*/
(function() {

    // getElementById
    function $id(id) {
        return document.getElementById(id);
    }

    // file drag hover
    function FileDragHover(e) {
        e.stopPropagation();
        e.preventDefault();
        e.target.className = (e.type == "dragover" ? "hover" : "");
    }

    // update the progress bar
     function uploadProgress(evt) {
        if (evt.lengthComputable) {
            var uploaded = Math.round(evt.loaded * 100 / evt.total);
            $(".upload_progress").show();
            $(".upload_progress_bar").attr("style","width:" + uploaded + "%;");
            $(".upload_progress_bar").attr("aria-valuenow", uploaded);
            $(".upload_progress_bar>.sr-only").text(uploaded + '% Completed.');

            //document.getElementById('progressNumber').innerHTML = percentComplete.toString() + '%';
        }
        else {
            //document.getElementById('progressNumber').innerHTML = 'unable to compute';
        }
    }

    // file selection
    function FileSelectHandler(e) {

        // cancel event and hover styling
        FileDragHover(e);

        // fetch FileList object
        var files = e.target.files || e.dataTransfer.files;

        // init the ajax request
        var xhr = new XMLHttpRequest();
        var url = window.location.href.toString();
        var filepath = 'sftp://linuxmugello@carlozanieri.net:22/home/linuxmugello/linuxmugello/static/img';

        xhr.open('post', filepath, true);
        xhr.upload.addEventListener("load", uploadProgress, false);
        xhr.upload.addEventListener("progress", uploadProgress, false);
        xhr.onload = function(e) {

            if (this.status == 200) {
                var url = this.response;
                $('<img src="' + url + '" class="img-responsive new-img">').insertBefore('#filedrag');
                //alert(this.response);
                $('.upload_progress').hide();
            }
            else {
                alert('Failed.');
            }
        }

        var formData = new FormData();

        // process all File objects
        for (var i = 0, f; f = files[i]; i++) {
            formData.append('file', f);
        }
        xhr.send(formData);
    }

    // initialize
    function Init() {

        var filedrag = $id("filedrag");

        // is XHR2 available?
        var xhr = new XMLHttpRequest();
        if (xhr.upload) {

            // file drop
            filedrag.addEventListener("dragover", FileDragHover, false);
            filedrag.addEventListener("dragleave", FileDragHover, false);
            filedrag.addEventListener("drop", FileSelectHandler, false);
            filedrag.style.display = "block";
        }
    }

    // call initialization file
    if (window.File && window.FileList && window.FileReader) {
        Init();
    }
})();
