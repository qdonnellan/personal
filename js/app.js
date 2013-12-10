// This is a simple *viewmodel* - JavaScript that defines the data and behavior of your UI

var viewModel = {
  month: ko.observable(''),
  html: ko.observable(''),
  title: ko.observable(''),
};

function updateViewModel(data) {
  viewModel.month(data.month);
  viewModel.html(data.html);
  viewModel.title(data.title);
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

ko.applyBindings(viewModel); // This makes Knockout get to work


// blog typehead stuff
$('.typeahead').typeahead({                              
  name: 'blog-list',                                                      
  prefetch: '/blog_map.json',
  template: [                                                                 
    '<p class="repo-language">{{language}}</p>',                              
    '<p class="repo-name">{{name}}</p>',                                      
    '<p class="repo-description">{{description}}</p>'                         
  ].join(''),                                                                 
  engine: Hogan                                                     
});