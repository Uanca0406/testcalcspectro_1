<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kalkulator Spektrofotometri</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/regression@2.0.1/dist/regression.min.js"></script>
    <style>
        .glassmorphism {
            background: rgba(255, 255, 255, 0.25);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.18);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        }
        .table-container {
            max-height: 400px;
            overflow-y: auto;
        }
        table {
            min-width: 100%;
        }
    </style>
</head>
<body class="bg-gradient-to-br from-blue-50 to-cyan-100 min-h-screen p-4">
    <div class="container mx-auto max-w-6xl">
        <header class="text-center mb-8">
            <h1 class="text-4xl font-bold text-blue-800 mb-2">Kalkulator Spektrofotometri</h1>
            <p class="text-blue-600">Perhitungan Konsentrasi, Regresi Linear, dan Parameter Validasi Metode</p>
        </header>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <!-- Input Data Standar -->
            <div class="glassmorphism rounded-xl p-6">
                <h2 class="text-2xl font-semibold text-blue-700 mb-4">Data Larutan Standar</h2>
                <div class="mb-4">
                    <label class="block text-blue-700 mb-2">Jumlah Standar:</label>
                    <input type="number" id="jumlah-standar" min="2" max="10" value="5" class="w-full p-2 border border-blue-300 rounded">
                </div>
                <div class="table-container">
                    <table class="w-full border-collapse">
                        <thead>
                            <tr class="bg-blue-100">
                                <th class="p-2 border text-left">No</th>
                                <th class="p-2 border text-left">Konsentrasi (ppm)</th>
                                <th class="p-2 border text-left">Absorbansi</th>
                            </tr>
                        </thead>
                        <tbody id="tabel-standar">
                            <!-- Data standar akan diisi oleh JavaScript -->
                        </tbody>
                    </table>
                </div>
                <button id="hitung-regresi" class="mt-4 bg-blue-600 hover:bg-blue-700 text-white py-2 px-4 rounded transition duration-300">
                    Hitung Regresi & Parameter
                </button>
            </div>

            <!-- Input Data Sampel -->
            <div class="glassmorphism rounded-xl p-6">
                <h2 class="text-2xl font-semibold text-blue-700 mb-4">Data Sampel</h2>
                <div class="mb-4">
                    <label class="block text-blue-700 mb-2">Jumlah Sampel:</label>
                    <input type="number" id="jumlah-sampel" min="1" max="20" value="3" class="w-full p-2 border border-blue-300 rounded">
                </div>
                <div class="table-container">
                    <table class="w-full border-collapse">
                        <thead>
                            <tr class="bg-blue-100">
                                <th class="p-2 border text-left">No</th>
                                <th class="p-2 border text-left">Gram Sampel</th>
                                <th class="p-2 border text-left">Absorbansi</th>
                                <th class="p-2 border text-left">Konsentrasi (ppm)</th>
                            </tr>
                        </thead>
                        <tbody id="tabel-sampel">
                            <!-- Data sampel akan diisi oleh JavaScript -->
                        </tbody>
                    </table>
                </div>
                <button id="hitung-konsentrasi" class="mt-4 bg-green-600 hover:bg-green-700 text-white py-2 px-4 rounded transition duration-300">
                    Hitung Konsentrasi Sampel
                </button>
            </div>
        </div>

        <!-- Hasil Perhitungan -->
        <div class="glassmorphism rounded-xl p-6 mt-6">
            <h2 class="text-2xl font-semibold text-blue-700 mb-4">Hasil Perhitungan</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                <!-- Hasil Regresi -->
                <div class="bg-white rounded-lg p-4 shadow">
                    <h3 class="text-xl font-medium text-blue-700 mb-2">Parameter Regresi Linear</h3>
                    <table class="w-full">
                        <tr>
                            <td class="p-2">Persamaan Regresi:</td>
                            <td class="p-2 font-mono" id="persamaan-regresi">y = a + bx</td>
                        </tr>
                        <tr>
                            <td class="p-2">Slope (b):</td>
                            <td class="p-2 font-mono" id="slope">-</td>
                        </tr>
                        <tr>
                            <td class="p-2">Intercept (a):</td>
                            <td class="p-2 font-mono" id="intercept">-</td>
                        </tr>
                        <tr>
                            <td class="p-2">Koefisien Korelasi (r):</td>
                            <td class="p-2 font-mono" id="koef-korelasi">-</td>
                        </tr>
                        <tr>
                            <td class="p-2">R-Squared (R²):</td>
                            <td class="p-2 font-mono" id="r-squared">-</td>
                        </tr>
                    </table>
                </div>

                <!-- Hasil Validasi -->
                <div class="bg-white rounded-lg p-4 shadow">
                    <h3 class="text-xl font-medium text-blue-700 mb-2">Parameter Validasi Metode</h3>
                    <table class="w-full">
                        <tr>
                            <td class="p-2">% RPD:</td>
                            <td class="p-2 font-mono" id="rpd">-</td>
                        </tr>
                        <tr>
                            <td class="p-2">% Akurasi:</td>
                            <td class="p-2 font-mono" id="akurasi">-</td>
                        </tr>
                        <tr>
                            <td class="p-2">Standard Error:</td>
                            <td class="p-2 font-mono" id="standard-error">-</td>
                        </tr>
                    </table>
                </div>
            </div>

            <!-- Grafik -->
            <div class="bg-white rounded-lg p-4 shadow">
                <h3 class="text-xl font-medium text-blue-700 mb-2">Grafik Kurva Kalibrasi</h3>
                <div class="h-64">
                    <canvas id="grafik-kalibrasi"></canvas>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Inisialisasi Chart
        const ctx = document.getElementById('grafik-kalibrasi').getContext('2d');
        let calibrationChart = new Chart(ctx, {
            type: 'scatter',
            data: {
                datasets: [{
                    label: 'Data Standar',
                    backgroundColor: 'rgb(59, 130, 246)',
                    borderColor: 'rgb(59, 130, 246)',
                    showLine: false,
                    pointRadius: 8,
                    pointHoverRadius: 10
                }, {
                    label: 'Garis Regresi',
                    backgroundColor: 'rgb(239, 68, 68)',
                    borderColor: 'rgb(239, 68, 68)',
                    showLine: true,
                    fill: false,
                    pointRadius: 0
                }]
            },
            options: {
                scales: {
                    x: {
                        title: {
                            display: true,
                            text: 'Konsentrasi (ppm)'
                        }
                    },
                    y: {
                        title: {
                            display: true,
                            text: 'Absorbansi'
                        }
                    }
                },
                responsive: true,
                maintainAspectRatio: false
            }
        });

        // Fungsi untuk mengisi tabel standar
        function isiTabelStandar() {
            const jumlahStandar = parseInt(document.getElementById('jumlah-standar').value);
            const tabelStandar = document.getElementById('tabel-standar');
            tabelStandar.innerHTML = '';

            // Contoh data standar (bisa diubah)
            const contohKonsentrasi = [0, 2, 4, 6, 8];
            const contohAbsorbansi = [0, 0.102, 0.201, 0.298, 0.402];

            for (let i = 0; i < jumlahStandar; i++) {
                const baris = document.createElement('tr');
                
                const no = document.createElement('td');
                no.className = 'p-2 border';
                no.textContent = i + 1;
                baris.appendChild(no);
                
                const konsentrasi = document.createElement('td');
                konsentrasi.className = 'p-2 border';
                const inputKonsentrasi = document.createElement('input');
                inputKonsentrasi.type = 'number';
                inputKonsentrasi.step = 'any';
                inputKonsentrasi.value = i < contohKonsentrasi.length ? contohKonsentrasi[i] : '';
                inputKonsentrasi.className = 'w-full p-1 border border-gray-300 rounded';
                inputKonsentrasi.dataset.param = 'konsentrasi';
                inputKonsentrasi.dataset.index = i;
                konsentrasi.appendChild(inputKonsentrasi);
                baris.appendChild(konsentrasi);
                
                const absorbansi = document.createElement('td');
                absorbansi.className = 'p-2 border';
                const inputAbsorbansi = document.createElement('input');
                inputAbsorbansi.type = 'number';
                inputAbsorbansi.step = 'any';
                inputAbsorbansi.value = i < contohAbsorbansi.length ? contohAbsorbansi[i] : '';
                inputAbsorbansi.className = 'w-full p-1 border border-gray-300 rounded';
                inputAbsorbansi.dataset.param = 'absorbansi';
                inputAbsorbansi.dataset.index = i;
                absorbansi.appendChild(inputAbsorbansi);
                baris.appendChild(absorbansi);
                
                tabelStandar.appendChild(baris);
            }
        }

        // Fungsi untuk mengisi tabel sampel
        function isiTabelSampel() {
            const jumlahSampel = parseInt(document.getElementById('jumlah-sampel').value);
            const tabelSampel = document.getElementById('tabel-sampel');
            tabelSampel.innerHTML = '';

            for (let i = 0; i < jumlahSampel; i++) {
                const baris = document.createElement('tr');
                
                const no = document.createElement('td');
                no.className = 'p-2 border';
                no.textContent = i + 1;
                baris.appendChild(no);
                
                const gram = document.createElement('td');
                gram.className = 'p-2 border';
                const inputGram = document.createElement('input');
                inputGram.type = 'number';
                inputGram.step = 'any';
                inputGram.className = 'w-full p-1 border border-gray-300 rounded';
                inputGram.dataset.param = 'gram';
                inputGram.dataset.index = i;
                gram.appendChild(inputGram);
                baris.appendChild(gram);
                
                const absorbansi = document.createElement('td');
                absorbansi.className = 'p-2 border';
                const inputAbsorbansi = document.createElement('input');
                inputAbsorbansi.type = 'number';
                inputAbsorbansi.step = 'any';
                inputAbsorbansi.className = 'w-full p-1 border border-gray-300 rounded';
                inputAbsorbansi.dataset.param = 'absorbansi';
                inputAbsorbansi.dataset.index = i;
                absorbansi.appendChild(inputAbsorbansi);
                baris.appendChild(absorbansi);
                
                const konsentrasi = document.createElement('td');
                konsentrasi.className = 'p-2 border';
                const inputKonsentrasi = document.createElement('input');
                inputKonsentrasi.type = 'number';
                inputKonsentrasi.step = 'any';
                inputKonsentrasi.className = 'w-full p-1 border border-gray-300 rounded';
                inputKonsentrasi.dataset.param = 'konsentrasi';
                inputKonsentrasi.dataset.index = i;
                inputKonsentrasi.readOnly = true;
                konsentrasi.appendChild(inputKonsentrasi);
                baris.appendChild(konsentrasi);
                
                tabelSampel.appendChild(baris);
            }
        }

        // Fungsi untuk mengambil data standar dari tabel
        function ambilDataStandar() {
            const jumlahStandar = parseInt(document.getElementById('jumlah-standar').value);
            const data = {
                konsentrasi: [],
                absorbansi: []
            };

            for (let i = 0; i < jumlahStandar; i++) {
                const inputKonsentrasi = document.querySelector(`input[data-param="konsentrasi"][data-index="${i}"]`);
                const inputAbsorbansi = document.querySelector(`input[data-param="absorbansi"][data-index="${i}"]`);

                if (inputKonsentrasi.value && inputAbsorbansi.value) {
                    data.konsentrasi.push(parseFloat(inputKonsentrasi.value));
                    data.absorbansi.push(parseFloat(inputAbsorbansi.value));
                }
            }

            return data;
        }

        // Fungsi untuk mengambil data sampel dari tabel
        function ambilDataSampel() {
            const jumlahSampel = parseInt(document.getElementById('jumlah-sampel').value);
            const data = {
                gram: [],
                absorbansi: []
            };

            for (let i = 0; i < jumlahSampel; i++) {
                const inputGram = document.querySelector(`input[data-param="gram"][data-index="${i}"]`);
                const inputAbsorbansi = document.querySelector(`input[data-param="absorbansi"][data-index="${i}"]`);

                if (inputGram.value && inputAbsorbansi.value) {
                    data.gram.push(parseFloat(inputGram.value));
                    data.absorbansi.push(parseFloat(inputAbsorbansi.value));
                }
            }

            return data;
        }

        // Fungsi untuk menghitung regresi linear
        function hitungRegresi() {
            const dataStandar = ambilDataStandar();
            
            if (dataStandar.konsentrasi.length < 2 || dataStandar.absorbansi.length < 2) {
                alert('Minimal diperlukan 2 data standar untuk menghitung regresi!');
                return;
            }

            // Menggunakan library regression.js untuk perhitungan regresi
            const points = dataStandar.konsentrasi.map((k, i) => [k, dataStandar.absorbansi[i]]);
            const result = regression.linear(points);

            // Menampilkan hasil
            document.getElementById('persamaan-regresi').textContent = `y = ${result.equation[1].toFixed(4)}x + ${result.equation[0].toFixed(4)}`;
            document.getElementById('slope').textContent = result.equation[1].toFixed(4);
            document.getElementById('intercept').textContent = result.equation[0].toFixed(4);
            document.getElementById('koef-korelasi').textContent = result.r.toFixed(4);
            document.getElementById('r-squared').textContent = result.r2.toFixed(4);

            // Menghitung RPD (Relative Percent Difference)
            const predictedAbsorbansi = dataStandar.konsentrasi.map(c => result.equation[0] + result.equation[1] * c);
            const residuals = dataStandar.absorbansi.map((a, i) => a - predictedAbsorbansi[i]);
            const meanAbsorbansi = dataStandar.absorbansi.reduce((sum, a) => sum + a, 0) / dataStandar.absorbansi.length;
            const rpd = (Math.sqrt(residuals.reduce((sum, r) => sum + r*r, 0) / (dataStandar.absorbansi.length - 2)) / meanAbsorbansi) * 100;
            document.getElementById('rpd').textContent = rpd.toFixed(2) + '%';

            // Menghitung akurasi (1 - RPD)
            document.getElementById('akurasi').textContent = (100 - rpd).toFixed(2) + '%';

            // Standard error
            const se = Math.sqrt(residuals.reduce((sum, r) => sum + r*r, 0) / (dataStandar.absorbansi.length - 2));
            document.getElementById('standard-error').textContent = se.toFixed(6);

            // Update grafik
            updateGrafik(dataStandar, result);
        }

        // Fungsi untuk mengupdate grafik
        function updateGrafik(dataStandar, result) {
            // Data titik standar
            calibrationChart.data.datasets[0].data = dataStandar.konsentrasi.map((k, i) => ({x: k, y: dataStandar.absorbansi[i]}));
            
            // Garis regresi (2 titik awal dan akhir)
            const minX = Math.min(...dataStandar.konsentrasi);
            const maxX = Math.max(...dataStandar.konsentrasi);
            calibrationChart.data.datasets[1].data = [
                {x: minX, y: result.equation[0] + result.equation[1] * minX},
                {x: maxX, y: result.equation[0] + result.equation[1] * maxX}
            ];
            
            calibrationChart.update();
        }

        // Fungsi untuk menghitung konsentrasi sampel
        function hitungKonsentrasi() {
            const dataStandar = ambilDataStandar();
            const dataSampel = ambilDataSampel();
            
            if (dataStandar.konsentrasi.length < 2 || dataStandar.absorbansi.length < 2) {
                alert('Hitung regresi standar terlebih dahulu!');
                return;
            }

            // Hitung regresi linear lagi untuk mendapatkan persamaan
            const points = dataStandar.konsentrasi.map((k, i) => [k, dataStandar.absorbansi[i]]);
            const result = regression.linear(points);
            const intercept = result.equation[0];
            const slope = result.equation[1];

            // Hitung konsentrasi untuk setiap sampel
            dataSampel.absorbansi.forEach((abs, i) => {
                const konsentrasi = (abs - intercept) / slope;
                document.querySelector(`input[data-param="konsentrasi"][data-index="${i}"]`).value = konsentrasi.toFixed(4);
            });
        }

        // Event listeners
        document.getElementById('jumlah-standar').addEventListener('change', isiTabelStandar);
        document.getElementById('jumlah-sampel').addEventListener('change', isiTabelSampel);
        document.getElementById('hitung-regresi').addEventListener('click', hitungRegresi);
        document.getElementById('hitung-konsentrasi').addEventListener('click', hitungKonsentrasi);

        // Inisialisasi tabel saat pertama kali load
        window.addEventListener('DOMContentLoaded', () => {
            isiTabelStandar();
            isiTabelSampel();
        });
    </script>
</body>
</html>
