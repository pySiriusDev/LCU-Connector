function Poetry-Add {
    [CmdletBinding()]
    
    param (
        [Parameter(Mandatory=$true)]
        [string]$lib_name
    )
    
    begin {

    }
    
    process {
        poetry.exe add $lib_name
    }
    
    end {
        Clear-Host
    }
}

function Poetry-Add-Dev {
    [CmdletBinding()]
    
    param (
        [Parameter(Mandatory=$true)]
        [string]$lib_name
    )
    
    begin {

    }
    
    process {
        poetry.exe add -G dev $lib_name
    }
    
    end {
        Clear-Host
    }
}

function Poetry-Remove {
    [CmdletBinding()]
    
    param (
        [Parameter(Mandatory=$true)]
        [string]$lib_name
    )
    
    begin {

    }
    
    process {
        poetry.exe remove $lib_name
    }
    
    end {
        Clear-Host
    }
}

function Poetry-Venv {
    [CmdletBinding()]
    
    param (
        
    )
    
    begin {

    }
    
    process {
        py.exe -m venv .venv
        poetry.exe shell
    }
    
    end {
        Clear-Host
    }
}

function Poetry-Install {
    [CmdletBinding()]
    
    param (
        
    )
    
    begin {

    }
    
    process {
        poetry.exe install
    }
    
    end {
        Clear-Host
    }
}

function Poetry-Shell {
    [CmdletBinding()]
    
    param (
        
    )
    
    begin {

    }
    
    process {
        poetry.exe shell
    }
    
    end {
        Clear-Host
    }
}

Set-Alias -Name pa -Value Poetry-Add -Force
Set-Alias -Name pad -Value Poetry-Add-Dev -Force
Set-Alias -Name prm -Value Poetry-Remove -Force
Set-Alias -Name pinst -Value Poetry-Install -Force
Set-Alias -Name pvenv -Value Poetry-Venv -Force
Set-Alias -Name pshl -Value Poetry-Shell -Force
