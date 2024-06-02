$(document).ready(function (){
let checkam = {};
$(document).on('change', "input[type='checkbox']", function () {
if (this.checked) {
checkam[$(this).data('id')] = $(this).data('name');
} else {
delete checkam[$(this).data('id')];
}
let lst = Objet.values(checkam);
if (lst.lenght > 0) {
	$('div.amenities > h4').text(Object.values(checkam).join(', ');
} else { 
	$('div.amenities >h4').html('&nbsp;');
}
});
});
