$(window).on('click', function (e) {
    suggestions_blocks = document.getElementsByClassName('suggestions')
    for (var el of suggestions_blocks) {
      el.style.display = 'none'
    }
  })
  // $(window).on('click keyup', function (e) {
  //   if (e.target.classList.contains('auto-search')) {
  //     model = e.target.id.split('-')[1]
  //     get_suggestions(e, app, model, e.target.value)
  //   }
  // })


  function get_suggestions(e){
    var suggestions_block = e.target.parentNode.querySelector('[id*="suggestions"]')
    var name = e.target.value
    console.log(name)
    $.ajax({
    type: "GET",
    url: suggestions_url,
    data: {
        name: name,
    },
    success: function(json) {
      console.log(json)
      if (json['result'] === '') {
        suggestions_block.style.display = 'none'
      } else {
        console.log(json['result'])
        suggestions_block.innerHTML = json['result']
        suggestions_block.style.display = 'block'
      }
    }
    })
}

  function set_suggestion_value(e) {
    var model
    for (var cls of e.target.classList) {
      if (cls.includes('suggestion-')) {
        model = cls.split('-')[1]
      }
    }
    input_el = e.target.parentNode.parentNode.querySelector('[id*="input-"]')
    input_el.setAttribute('data-slug', e.target.dataset.slug)
    input_el.value = e.target.innerText
    var event = new Event('change');
    input_el.dispatchEvent(event)    
  }


  function go_to_suggestion(app, slug){
    if (compare === true){
      var slug_1 = window.location.split()
      var url = window.location.origin + '/' + app + '/'
    }
    var url = window.location.origin + '/' + app + '/' + slug + '/'
    window.location = url
  }

