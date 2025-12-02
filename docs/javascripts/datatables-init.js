/* assets/js/datatables-init.js */
document.addEventListener('DOMContentLoaded', function () {
    // Prüfen, ob das Ziel‑Element existiert
    const $table = $('#charts-table');   // ID‑basiert – bei Markdown‑Tabellen ggf. anpassen
    if ($table.length === 0) {
        console.warn('DataTables: Keine Tabelle mit id="charts-table" gefunden.');
        return;
    }

    $table.DataTable({
        // Grundlegende Optionen – anpassen nach Bedarf
        paging: true,
        pageLength: 25,
        lengthMenu: [10, 25, 50, 100],
        ordering: true,
        order: [[2, 'desc']],           // Standard‑Sortierung nach „Besitzer“ absteigend
        searching: true,
        responsive: true,               // Für mobiles Layout
        // Bootstrap‑Styling aktivieren (falls du das Bootstrap‑Theme eingebunden hast)
        dom: '<"top"lf>rt<"bottom"ip><"clear">',

        // Spalten‑Definitionen (optional, z. B. Zahlen‑Sortierung)
        columnDefs: [
            { targets: 0, width: '40px' },      // Rang‑Spalte
            { targets: 2, type: 'num-fmt' },   // Besitzer‑Spalte als Zahl formatieren
            { targets: 3, type: 'num-fmt' }    // Preis‑Spalte als Zahl formatieren
        ],

        // Sprache anpassen (Deutsch)
        language: {
            url: 'https://cdn.datatables.net/plug-ins/1.13.6/i18n/de-DE.json'
        },

        // Such‑Panes konfigurieren
        layout: {
            top1: {
                searchPanes: {
                    viewTotal: true
                }
            }
        }
    });

    const $tableType = $('#type-table');   // ID‑basiert – bei Markdown‑Tabellen ggf. anpassen
    if ($tableType.length === 0) {
        console.warn('DataTables: Keine Tabelle mit id="type-table" gefunden.');
        return;
    }

    $tableType.DataTable({
        initComplete: function () {
            this.api()
            .columns()
            .every(function () {
                let column = this;
 
                // Create select element
                let select = document.createElement('select');
                select.add(new Option(''));
                column.footer().replaceChildren(select);
 
                // Apply listener for user change in value
                select.addEventListener('change', function () {
                    column
                        .search(select.value, {exact: true})
                        .draw();
                });
 
                // Add list of options
                column
                    .data()
                    .unique()
                    .sort()
                    .each(function (d, j) {
                        select.add(new Option(d));
                    });
            });
        },
        // Grundlegende Optionen – anpassen nach Bedarf
        paging: true,
        pageLength: 50,
        lengthMenu: [10, 25, 50, 100],
        ordering: true,
        order: [[0, 'asc']],           // Standard‑Sortierung nach „Code“ aufsteigend
        searching: true,
        responsive: true,               // Für mobiles Layout
        // Bootstrap‑Styling aktivieren (falls du das Bootstrap‑Theme eingebunden hast)
        dom: '<"top"lf>rt<"bottom"ip><"clear">',
        // Spalten‑Definitionen (optional, z. B. Zahlen‑Sortierung)
        columnDefs: [
            { targets: 0, width: '150px' }      // Code‑Spalte
        ],
        // Sprache anpassen (Deutsch)
        language: {
            url: 'https://cdn.datatables.net/plug-ins/1.13.6/i18n/de-DE.json'
        },
        // Such‑Panes konfigurieren
        layout: {
            top1: {
                searchPanes: {
                    viewTotal: true
                }
            }
        }
    });

});