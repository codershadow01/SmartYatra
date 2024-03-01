// document.addEventListener("DOMContentLoaded", function() {

//     // Dummy data
//     // const dummyData = [
//     //   {"id": 1, "source": "Lanka", "distination": "Cantt", "mode": "AC123","ETA": 30, "at": 10, "cost": 10},
//     //   {"id": 2, "source": "Lanka", "distination": "Cantt", "mode": "AC123","ETA": 30, "at": 10, "cost": 10},
//     //   {"id": 3, "source": "Lanka", "distination": "Cantt", "mode": "AC123","ETA": 30, "at": 10, "cost": 10},
//     //   {"id": 4, "source": "Lanka", "distination": "Cantt", "mode": "AC123","ETA": 30, "at": 10, "cost": 10},
//     //   {"id": 5, "source": "Lanka", "distination": "Cantt", "mode": "AC123","ETA": 30, "at": 10, "cost": 10},
//     //   {"id": 6, "source": "Lanka", "distination": "Cantt", "mode": "AC123","ETA": 30, "at": 10, "cost": 10},
//     //   {"id": 7, "source": "Lanka", "distination": "Cantt", "mode": "AC123","ETA": 30, "at": 10, "cost": 10},
//     //   {"id": 8, "source": "Lanka", "distination": "Cantt", "mode": "AC123","ETA": 30, "at": 10, "cost": 10},
//     // ];
//     // var routesDataElement = document.getElementById('routes-data');
//     // if (routesDataElement) {
//     //   var routesData = JSON.parse(routesDataElement.value);
//     //   console.log(routesData);  // Use routesData in your JavaScript
//     // }
//     // Function to insert data into the table
//     function insertData(routesData) {
//       console.log(routesData);
//       const tableBody = document.getElementById('data-body');
//       routesData.forEach(item => {
//         const row = document.createElement('tr');
//         row.innerHTML = `
//           <td>${item.mode}</td>
//           <td>${item.ETA}</td>
//           <td>${item.at}</td>
//           <td>${item.cost}</td>
//           <!-- Button to toggle collapse detail -->
//         <button class="btn btn-success" type="button" data-bs-toggle="collapse" data-bs-target="#detail${item.id}" aria-expanded="false" aria-controls="detail${item.id}">
//           Show Details
//         </button>
//         `;
//         tableBody.appendChild(row);

//         // Create collapse detail for each row
//     const detailRow = document.createElement('tr');
//     detailRow.innerHTML = `
//       <!--  <td colspan="5"> -->
//         <div class="collapse" id="detail${item.id}">
//           <div class="card card-body">
//             <!-- Detail content here -->
//             Detail for ${item.distination}
//           </div>
//         </div>
//       <!-- </td>  -->
//     `;
//     tableBody.appendChild(detailRow);
//       });
//     }
  
//     insertData();
//   });

document.addEventListener("DOMContentLoaded", function() {
   
  function extractData(dataString) {
    // Remove square brackets and split by '), (' to get routess
    var routess = dataString.slice(2, -2).split("), (");
    var routesDataValues = [];
    // Loop through routess
    routess.forEach(function(routesString) {
        // Remove parentheses and split by comma to get values
        var routesValues = routesString.replace(/[\(\)]/g, '').split(", ");
        var routes = routesValues.map(function(value) {
            // If the value is numeric, parse it as float
            return isNaN(value) ? value : parseFloat(value);
        });
        routesDataValues.push(routes);
    });
    return routesDataValues;
}

  console.log(" i am in planner,js");
  
  var routesDataElements = document.getElementById('routes-data');
  var routesDataValues = extractData(routesDataElements.value);

  console.log(routesDataValues)
  
  function insertData(routesDataValues) {
      const tableBody = document.getElementById('data-body');
      routesDataValues.forEach((routes)=> {

          console.log("i am in first loop");

          const row = document.createElement('tr');
          row.innerHTML = `
              <td>${routes[0]}</td>
              <td>${routes[2]}</td>
              <td>${routes[3]}</td>
          
          `;
          tableBody.appendChild(row);

          const detailRow = document.createElement('tr');
          detailRow.innerHTML = `
              <td colspan="5">
                  <div class="collapse" id="detail${item.id}">
                      <div class="card card-body">
                          Detail for ${routes[4]}
                      </div>
                  </div>
              </td>
          `;
          tableBody.appendChild(detailRow);
      });
  }

  insertData(routesDataValues);
});