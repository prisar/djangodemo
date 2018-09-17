(function () {
    'use script';
    
    angular.module('scrumboard.demo').run(['$http', run]);
    
    function run($http) {
        $http.defaults.xsrfHeaderName = "X-CSRFToken";
        $http.defaults.xsrfCookieName = "csrftoken";
    }
})();