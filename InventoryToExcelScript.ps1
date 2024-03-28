#--------POPULATE BLANK CSV FILE WITH COLUMN HEADERS--------------  

# store the username in a variable
$username = $env:USERNAME 

# Define column names (replace with your desired names)
$column1 = "System Name"
$column2 = "Serial Number"
$column3 = "Model"

# Create CSV content string
$csvContent = "$column1,$column2,$column3`n"  # "`n` represents a new line

# Path to the new CSV file (replace with your desired path)
$filePath = "C:\Users\$username\Powershell\SerialNumberWarrantyData.csv"

# Write content to the CSV file
Out-File -FilePath $filePath -InputObject $csvContent -Encoding UTF8

Write-Host "Successfully created a CSV file with column headers: $column1 and $column2 and $column3"

# Imports SendKeys mthod from .NET framework
# to send keystrokes to active windows
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.SendKeys]::SendWait("{ENTER}")

# HERE WE WANT TO AUTOFIT COLUMN WIDTH

# open the excel file from the powerhell cmd line 
ii SerialNumberWarrantyData.csv
 

# ----------ADDS DATA TO CSV COLUMNS--------------------------------------------

# STEP 2 Lookup serial Number of current computer and add it to the CSV file 

# store the username in a variable
$username = $env:USERNAME    

# Get system name and serial number 
$computerName = (Get-WmiObject Win32_ComputerSystem).Name
$serialNumber = (Get-WmiObject Win32_Bios).SerialNumber
$model = (Get-CimInstance -ClassName Win32_ComputerSystem).Model 

# Path to your existing CSV file (modify as needed)
$filePath = "C:\Users\$username\Powershell\SerialNumberWarrantyData.csv"

# Create objects for system informationI
$data = New-Object PSObject -Property @{
  "System Name" = $computerName
  "Serial Number" = $serialNumber
  "Model" = $model
}

# Append data to CSV file
Export-Csv -Path $filePath -InputObject $data -Append -NoTypeInformation

# Informative message
Write-Host "System name, serial number, and model added to '$filePath'"

# Imports SendKeys mthod from .NET framework
# to send keystrokes to active windows
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.SendKeys]::SendWait("{ENTER}")

ii SerialNumberWarrantyData.csv