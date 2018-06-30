$('.fa-plus').on('click', function(){
$('#form').slideDown()
$('.add').hide()
$('.action').show()
})

$('.fa-check').on('click', function(){
  if ($('#id_title').val() == "" || $('#id_content').val() == "" || $('#id_author').val() == "") return alert('All fields are mandatory.')
  $('#form form').submit()
})

$('.fa-times').on('click', function(){
$('#form form')[0].reset()
$('#form').slideUp()
$('.add').show()
$('.action').hide()
})

