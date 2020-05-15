$.ajax({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  datatype: 'JSON',
  success: function (data) {
    $('#hello').text(data.hello);
  }
});
