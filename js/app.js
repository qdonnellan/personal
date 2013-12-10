// This is a simple *viewmodel* - JavaScript that defines the data and behavior of your UI

var viewModel = {
  month: ko.observable(''),
  year: ko.observable(''),
  day: ko.observable(''),
  html: ko.observable('<h1 class="text-muted"><i class="fa fa-cog fa-spin"></i> loading...</h1>'),
  title: ko.observable('')
};

function updateViewModel(data) {
  viewModel.month(data.month);
  viewModel.html(data.html);
  viewModel.title(data.title);
  viewModel.year(data.year);
  viewModel.day(data.day);
}

$.getJSON("/api/blog/latest", function (result) {
    updateViewModel(result)
  });

// retriece the blog when its link is clicked
// link will contain a rel attribute that looks like /api/blog/2013/07/21
// this attribute identifies the blog when the api call is made
$(".blog-link").click(function () {
  blog_ref = $(this).attr("rel")
  $.getJSON(blog_ref, function (result) {
    updateViewModel(result)
  });
});

// blog typehead stuff
$('#blog .typeahead').typeahead({                              
  name: 'blog-list',                                                      
  prefetch: '/blogmap.json',
  template: [                                                           
    '<p class="tt-blog-name">{{name}}</p>',                                      
    '<p class="tt-blog-date">{{date}}</p>'                         
  ].join(''),                                                                 
  engine: Hogan                                             
});

$('#search-input').bind('typeahead:selected', function(obj, datum, name) {      
    blog_ref = datum.reference;
    $.getJSON(blog_ref, function (result) {
      updateViewModel(result)
    });
});

ko.applyBindings(viewModel); // This makes Knockout get to work
