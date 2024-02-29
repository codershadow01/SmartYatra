document.addEventListener("DOMContentLoaded", function() {

    // Dummy data
    const dummyData = [
      {"id": 1, "source": "Lanka", "distination": "Cantt", "mode": "AC123","ETA": 30, "at": 10, "cost": 10},
      {"id": 2, "source": "Lanka", "distination": "Cantt", "mode": "AC123","ETA": 30, "at": 10, "cost": 10},
      {"id": 3, "source": "Lanka", "distination": "Cantt", "mode": "AC123","ETA": 30, "at": 10, "cost": 10},
      {"id": 4, "source": "Lanka", "distination": "Cantt", "mode": "AC123","ETA": 30, "at": 10, "cost": 10},
      {"id": 5, "source": "Lanka", "distination": "Cantt", "mode": "AC123","ETA": 30, "at": 10, "cost": 10},
      {"id": 6, "source": "Lanka", "distination": "Cantt", "mode": "AC123","ETA": 30, "at": 10, "cost": 10},
      {"id": 7, "source": "Lanka", "distination": "Cantt", "mode": "AC123","ETA": 30, "at": 10, "cost": 10},
      {"id": 8, "source": "Lanka", "distination": "Cantt", "mode": "AC123","ETA": 30, "at": 10, "cost": 10},
    ];
  
    // Function to insert data into the table
    function insertData() {
      const tableBody = document.getElementById('data-body');
      dummyData.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
          <td>${item.mode}</td>
          <td>${item.ETA}</td>
          <td>${item.at}</td>
          <td>${item.cost}</td>
          <!-- Button to toggle collapse detail -->
        <button class="btn btn-success" type="button" data-bs-toggle="collapse" data-bs-target="#detail${item.id}" aria-expanded="false" aria-controls="detail${item.id}">
          Show Details
        </button>
        `;
        tableBody.appendChild(row);

        // Create collapse detail for each row
    const detailRow = document.createElement('tr');
    detailRow.innerHTML = `
      <!--  <td colspan="5"> -->
        <div class="collapse" id="detail${item.id}">
          <div class="card card-body">
            <!-- Detail content here -->
            Detail for ${item.distination}
          </div>
        </div>
      <!-- </td>  -->
    `;
    tableBody.appendChild(detailRow);
      });
    }
  
    insertData();
  });
  