Sub �e�X�g()
    
  Set book1 = Workbooks.Add
  book1.Sheets.Add
 

  Dim objSheet
    Dim k As Long
    Dim i As Long
    k = 1
    
    Dim m As Long
    m = 0
    
  ' �u�b�N�̑S�V�[�g�� 1 �����[�v���ď�������
  For Each objSheet In ThisWorkbook.Worksheets
    m = m + 1
    Debug.Print objSheet.Name & "���������܂�"
    book1.Sheets("sheet1").Cells(k, 1) = objSheet.Name
    'A1�Z���ɃV�[�g�̖��O����������
    'objSheet.Cells(1, 1) = "���̃V�[�g�̖��O��" & objSheet.Name & "�ł��B"
    
    Debug.Print objSheet.Cells(Rows.Count, 2).End(xlUp).Row & "�ő�s"

    Dim s As String
    s = ""
    For i = 2 To objSheet.Cells(Rows.Count, 2).End(xlUp).Row
        book1.Sheets("sheet1").Cells(k, 1) = objSheet.Name
        For j = 2 To 6
            book1.Sheets("sheet1").Cells(k, j) = objSheet.Cells(i, j)
        Next j
        s = s & " " & objSheet.Cells(i, 2)
        k = k + 1
    Next i
    book1.Sheets("sheet2").Cells(m, 1) = m
    book1.Sheets("sheet2").Cells(m, 2) = objSheet.Cells(2, 2) & " " & objSheet.Cells(3, 2) & " " & objSheet.Cells(4, 2)
    book1.Sheets("sheet2").Cells(m, 3) = s
    
    
  Next
 
    
End Sub