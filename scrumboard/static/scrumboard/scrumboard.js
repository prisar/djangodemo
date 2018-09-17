(function() {
    'use strict';

    angular.module('scrumboard.demo', [])
        .controller('ScrumboardController', ['$scope', '$http', ScrumboardController]);

    function ScrumboardController($scope, $http) {
        $scope.add = function(list, title) {
            var card = {
                list: list.id,
                title: title
            };
            
            $http.post("scrumboard/cards/", card)
                .then(function (response) {
                    list.cards.push(response.data);
                },
                function () {
                    alert('Could not create card');
                });
            
        };
        
        $scope.login = function () {
            $http.post('/auth_api/login/',
                {username: 'admin', password: 'Ril@1234'})
        }
        
        $scope.data = [];
        $http.get("/scrumboard/lists/").then(function(reponse){
            $scope.data = reponse.data;
        });
    }
}());