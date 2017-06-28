/**
 * Created by Yash Bidasaria on 5/23/2017.
 */
var app = angular.module("app", ['ngRoute'])
    .config(['$routeProvider', '$locationProvider',
        function($routeProvider, $locationProvider) {
            $routeProvider
                .when('/buyer2', {
                    templateUrl: 'buyer2.html',
                    controller: 'buyer2',
                    controllerAs: 'buyer2'
                }).when('/buyer_new', {
                templateUrl: 'buyer_new_partial.html',
                controller: 'buyer1',
                controllerAs: 'buyer1'
            }).otherwise({
                redirectTo: '/buyer_new'
            });
        }]);

app.service('shared', function() {
    var db_ch = {
        name: "app",
        info: "",
        price: 0,
        schema: ""
    }

    return {
        getProp: function() {
           return db_ch;
        },
        setProp: function(name, info, price, schema) {
            db_ch.name = name;
            db_ch.info = info;
            db_ch.price = price;
            db_ch.schema = schema;
            console.log("in shared " + name);
        }
    }
})

app.controller("buyer1", ['$scope', '$rootScope', '$http', 'shared','$route', '$routeParams', '$location',
    function($scope, $rootScope, $http, shared, $route, $routeParams, $location) {
    $scope.sellers = [

    ];
    $scope.budget = 0;
    $scope.choice = {
        name: "",
        num: 0
    };
    $scope.total = 0;
    $scope.databases = [
        {
            name: "X",
            info: "info",
            price: 12,
            schema: "23"
       },
        {
            name: "Y",
            info: "info",
            price: 12,
            schema: "24"
        }

    ];
    $rootScope.db_choice = {
        name : "initial",
        info : "",
        price: 0,
        schema: ""
    };
    $scope.sellerChoice = function(choice){
        $scope.choice.name = choice.name;
        $scope.choice.num = choice.num;
    };
    $scope.getSellers = function(){
        //get the current sellers. Populated the variable sellers
    };
    $scope.getDBs = function(seller) {
        //have seller get databases. Polulate the variable databases.
        return databases;
    };
    $scope.getQuery = function(query) {
        //check if valid query
        //update total amount
        //get query, return all the corresponding data
        return a;
    };
    $scope.reset = function reset() {
        choice = "";
        total = 0;
        choice.name = "";
        choice.num = 0;

    };

    $http({
        method: "GET",
        url: "127.0.0.1:8000"
    }).then(function success(response){
        $scope.databases = angular.fromJson(response.data);
        console.log("status: " + response.status)
    }).catch(function (response) {
        console.log("Error occured: " + response.status)
    }).finally(function (){
        console.log("task finished");
    });

    $scope.removeInfo = function() {
        var myNode = document.getElementById("info");
        while (myNode.firstChild) {
            myNode.removeChild(myNode.firstChild);
        }
    };

    $scope.addInfo = function(db) {
        $scope.removeInfo();
        $rootScope.db_choice.name = db.name;
        $rootScope.db_choice.info = db.info;
        $rootScope.db_choice.schema = db.schema;
        $rootScope.db_choice.price = db.price;
        shared.setProp(db.name, $rootScope.db_choice.info, $rootScope.db_choice.price, $rootScope.db_choice.schema)

        var seller = document.createElement('p');
        var bold1 = document.createElement('b');
        seller.appendChild(bold1);
       bold1.append(document.createTextNode("Seller: " + $scope.sellerChoice.name));
       var db = document.createElement('p');
       db.append(document.createTextNode("Dataset Name:" + $rootScope.db_choice.name));
       console.log($rootScope.db_choice.name);
       var description = document.createElement('p');
       description.append(document.createTextNode("Description: " + $rootScope.db_choice.info));
       var schema = document.createElement('p');
       schema.append(document.createTextNode("Schema: " + $rootScope.db_choice.schema));
       var price = document.createElement('p');
       price.append(document.createTextNode("Dataset Price: " + $rootScope.db_choice.price));

        document.getElementById("info").appendChild(seller);
        document.getElementById("info").appendChild(db);
        document.getElementById("info").appendChild(description);
        document.getElementById("info").appendChild(schema);
        document.getElementById("info").appendChild(price);

    }
}]);

app.controller("buyer2", ['$scope', '$rootScope', 'shared', '$routeParams',
    function($scope, $rootScope, shared, $routeParams) {

    $scope.choice = {
     name: "",
     info: "",
     price: 0,
     schema: ""
     };


    $scope.checkSQL = function(query) {
        console.log("HELLO");
        console.log(query);
        console.log(
            SQLParser.parse('select from test where a = 1 and foo = "bar"').toString());

    };

    $scope.choice = shared.getProp();
    console.log("choice =" + $scope.choice.name);

}]);
