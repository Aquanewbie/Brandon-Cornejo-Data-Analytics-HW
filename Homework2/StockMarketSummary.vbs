Sub StockMarketSummary()
'Loop through all Sheets'
Dim ws As Worksheet
For Each ws In Worksheets



        'Add Ticker to Cells (1,9)'
        'Add Yearly Change to (1,10)'
        'Add Percent Change to (1,11)'
        'Add Total Stock Volume to (1,12)'

        ws.Cells(1, 9).Value = "Ticker"
        ws.Cells(1, 10).Value = "Yearly Change"
        ws.Cells(1, 11).Value = "Percent Change"
        ws.Cells(1, 12).Value = "Total Stock Volume"

        'Widen Columns I,J,K,L'
        ws.Columns("I:L").AutoFit
        ws.Columns("J").NumberFormat = "0.00"
        
        'Loop Through Unique Value and Document them in Ticker Column(9)'
        
        lastrow = ws.Cells(Rows.Count, 1).End(xlUp).Row
        For i = 1 To lastrow
            If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
            Dim lastrowticker As Long
            lastrowticker = ws.Cells(Rows.Count, 9).End(xlUp).Row + 1
            ws.Cells(lastrowticker, 9).Value = Cells(i + 2, 1).Value
            End If
        Next i
        
        'Determine Yearly Change and Percetange Change'
        lastrow2 = ws.Cells(Rows.Count, 1).End(xlUp).Row
        For j = 1 To lastrow2
            If ws.Cells(j + 1, 1).Value <> ws.Cells(j, 1).Value Then
                Dim openprice As Double
                Dim closeprice As Double
                openprice = Cells(j + 1, 1).Offset(0, 2).Value
                closeprice = Cells(j + 1, 1).Offset(261, 5).Value
                lastrowchange = ws.Cells(Rows.Count, 10).End(xlUp).Row + 1
                ws.Cells(lastrowchange, 10).Value = closeprice - openprice
                lastrowpercent = ws.Cells(Rows.Count, 11).End(xlUp).Row + 1
                If openprice <> 0 Then
                ws.Cells(lastrowpercent, 11).Value = (closeprice - openprice) / openprice
                Else
                ws.Cells(lastrowpercent, 11).Value = "N/A"
                End If
                
                'Total Volume for each Ticker'
                TotalVolume = Application.Sum(Range(ws.Cells(j + 1, 7), ws.Cells(j + 262, 7)))
                lastrowvolume = ws.Cells(Rows.Count, 12).End(xlUp).Row + 1
                ws.Cells(lastrowvolume, 12).Value = TotalVolume
            
            End If
        Next j
        
        'Color indicate the rows of Percentages'
       lastrow3 = ws.Cells(Rows.Count, 1).End(xlUp).Row
        For c = 1 To lastrow3
            If ws.Cells(c + 1, 11).Value > 0 Then
            ws.Cells(c + 1, 11).Interior.ColorIndex = 4
            ElseIf ws.Cells(c + 1, 11).Value < 0 Then
            ws.Cells(c + 1, 11).Interior.ColorIndex = 3
            End If
        Next c
        
        'Format Percentages to 00.00%'
        ws.Range("K:K").NumberFormat = "0.00%"
       
Next ws

    
End Sub