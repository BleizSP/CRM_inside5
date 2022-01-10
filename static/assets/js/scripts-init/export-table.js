$(function() {
$("#btn-export").click(function(e){
var table = $("#bank-operation-list");
if(table && table.length){
$(table).table2excel({
exclude: ".noExl",
name: "Excel Document Name",
filename: "BBBootstrap" + new Date().toISOString().replace(/[\-\:\.]/g, "") + ".xls",
fileext: ".xls",
exclude_img: true,
exclude_links: true,
exclude_inputs: false,
preserveColors: false
});
}
});

});