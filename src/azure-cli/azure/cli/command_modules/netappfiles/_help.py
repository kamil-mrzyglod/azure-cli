# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps

# pylint: disable=line-too-long


helps['netappfiles'] = """
    type: group
    short-summary: Manage Azure NetApp Files (ANF) Resources.
"""

# account

helps['netappfiles account'] = """
    type: group
    short-summary: Manage Azure NetApp Files (ANF) Account Resources.
"""

helps['netappfiles account create'] = """
    type: command
    short-summary: Create a new Azure NetApp Files (ANF) account. Note that active directories are added using the subgroup commands.
    parameters:
        - name: --account-name --name -a -n
          short-summary: The name of the ANF account
        - name: --tags
          short-summary: Space-separated tags in `key[=value]` format
    examples:
        - name: Create an ANF account
          text: >
            az netappfiles account create -g mygroup --name myname -l location --tags testtag1=mytag1 testtag3=mytagg
"""

helps['netappfiles account update'] = """
    type: command
    short-summary: Set/modify the tags for a specified ANF account.
    parameters:
        - name: --account-name --name -a -n
          short-summary: The name of the ANF account
        - name: --tags
          short-summary: Space-separated tags in `key[=value]` format
    examples:
        - name: Update the tags of an ANF account
          text: >
            az netappfiles account update -g mygroup --name myname --tags testtag2=mytagb
"""

helps['netappfiles account delete'] = """
    type: command
    short-summary: Delete the specified ANF account.
    parameters:
        - name: --account-name --name -a -n
          short-summary: The name of the ANF account
    examples:
        - name: Delete an ANF account
          text: >
            az netappfiles account delete -g mygroup --name myname
"""

helps['netappfiles account list'] = """
    type: command
    short-summary: List ANF accounts.
    examples:
        - name: List ANF accounts within a resource group
          text: >
            az netappfiles account list -g mygroup
"""

helps['netappfiles account show'] = """
    type: command
    short-summary: Get the specified ANF account.
    parameters:
        - name: --account-name --name -a -n
          short-summary: The name of the ANF account
    examples:
        - name: Get an ANF account
          text: >
            az netappfiles account show -g mygroup --name myname
"""

# account active directory subgroup commands

helps['netappfiles account ad'] = """
    type: group
    short-summary: Manage Azure NetApp Files (ANF) Account active directories.
"""

helps['netappfiles account ad add'] = """
    type: command
    short-summary: Add an active directory to the account.
    parameters:
        - name: --account-name --name -a -n
          short-summary: The name of the ANF account
        - name: --username
          short-summary: Username of Active Directory domain administrator
        - name: --password
          short-summary: Plain text password of Active Directory domain administrator
        - name: --domain
          short-summary: Name of the Active Directory domain
        - name: --dns
          short-summary: Comma separated list of DNS server IP addresses for the Active Directory domain
        - name: --smb-server-name
          short-summary: NetBIOS name of the SMB server. This name will be registered as a computer account in the AD and used to mount volumes. Must be 10 characters or less
        - name: --organizational-unit
          short-summary: The Organizational Unit (OU) within the Windows Active Directory
    examples:
        - name: Add an active directory to the account
          text: >
            az netappfiles account ad add -g mygroup --name myname --username aduser --password aduser --smb-server-name SMBSERVER --dns 1.2.3.4 --domain westcentralus
"""

helps['netappfiles account ad list'] = """
    type: command
    short-summary: List the active directories of an account.
    parameters:
        - name: --account-name --name -a -n
          short-summary: The name of the ANF account
    examples:
        - name: Add an active directory to the account
          text: >
            az netappfiles account ad list -g mygroup --name myname
"""

helps['netappfiles account ad remove'] = """
    type: command
    short-summary: Remove an active directory from the account.
    parameters:
        - name: --account-name --name -a -n
          short-summary: The name of the ANF account
        - name: --active-directory
          short-summary: The id of the active directory
    examples:
        - name: Remove an active directory from the account
          text: >
            az netappfiles account ad remove -g mygroup --name myname --active-directory 13641da9-c0e9-4b97-84fc-4f8014a93848
"""


# pools

helps['netappfiles pool'] = """
    type: group
    short-summary: Manage Azure NetApp Files (ANF) Pool Resources.
"""

helps['netappfiles pool create'] = """
    type: command
    short-summary: Create a new Azure NetApp Files (ANF) pool.
    parameters:
        - name: --account-name -a
          short-summary: The name of the ANF account
        - name: --name --pool-name -n -p
          short-summary: The name of the ANF pool
        - name: --size
          short-summary: The size for the ANF pool. Must be an integer number of tebibytes in multiples of 4
        - name: --service-level
          short-summary: The service level for the ANF pool
        - name: --tags
          short-summary: Space-separated tags in `key[=value]` format
    examples:
        - name: Create an ANF pool
          text: >
            az netappfiles pool create -g mygroup --account-name myaccountname --name mypoolname -l westus2 --size 8 --service-level premium
"""

helps['netappfiles pool update'] = """
    type: command
    short-summary: Update the tags of the specified ANF pool.
    parameters:
        - name: --account-name -a
          short-summary: The name of the ANF account
        - name: --name --pool-name -n -p
          short-summary: The name of the ANF pool
        - name: --size
          short-summary: The size for the ANF pool. Must be an integer number of tebibytes in multiples of 4
        - name: --service-level
          short-summary: The service level for the ANF pool
        - name: --tags
          short-summary: Space-separated tags in `key[=value]` format
    examples:
        - name: Update specific values for an ANF pool
          text: >
            az netappfiles pool update -g mygroup --account-name myaccname --name mypoolname --service-level ultra --tags mytag1=abcd mytag2=efgh
"""

helps['netappfiles pool delete'] = """
    type: command
    short-summary: Delete the specified ANF pool.
    parameters:
        - name: --account-name -a
          short-summary: The name of the ANF account
        - name: --name --pool-name -n -p
          short-summary: The name of the ANF pool
    examples:
        - name: Delete an ANF pool
          text: >
            az netappfiles pool delete -g mygroup --account-name myaccname --name mypoolname
"""

helps['netappfiles pool list'] = """
    type: command
    short-summary: L:ist the ANF pools for the specified account.
    parameters:
        - name: --account-name -a
          short-summary: The name of the ANF account
    examples:
        - name: List the pools for the ANF account
          text: >
            az netappfiles pool list -g mygroup --account-name myname
"""

helps['netappfiles pool show'] = """
    type: command
    short-summary: Get the specified ANF pool.
    parameters:
        - name: --account-name -a
          short-summary: The name of the ANF account
        - name: --name --pool-name -n -p
          short-summary: The name of the ANF pool
    examples:
        - name: Get an ANF pool
          text: >
            az netappfiles pool show -g mygroup --account-name myaccname --name mypoolname
"""

# volumes

helps['netappfiles volume'] = """
    type: group
    short-summary: Manage Azure NetApp Files (ANF) Volume Resources.
"""

helps['netappfiles volume create'] = """
    type: command
    short-summary: Create a new Azure NetApp Files (ANF) volume. Export policies are applied with the subgroup commands but note that volumes are always created with a default export policy
    parameters:
        - name: --account-name -a
          short-summary: The name of the ANF account
        - name: --pool-name -p
          short-summary: The name of the ANF pool
        - name: --name --volume-name -n -v
          short-summary: The name of the ANF volume
        - name: --service-level
          short-summary: The service level
        - name: --usage-threshold
          short-summary: The maximum storage quota allowed for a file system as integer number of GiB. Min 100 GiB, max 100TiB"
        - name: --creation-token
          short-summary: A 1-80 character long alphanumeric string value that identifies a unique file share or mount point in the target subnet
        - name: --vnet
          short-summary: The vnet for the volume
        - name: --subnet
          short-summary: The subnet. If omitted 'default' will be used
        - name: --protocol-types
          short-summary: Space seperated list of protocols that the volume can use
        - name: --tags
          short-summary: Space-separated tags in `key[=value]` format
    examples:
        - name: Create an ANF volume
          text: >
            az netappfiles volume create -g mygroup --account-name myaccname --pool-name mypoolname --name myvolname -l westus2 --service-level premium --usage-threshold 100 --creation-token "unique-file-path" --vnet myvnet --subnet mysubnet --protocol-types NFSv3 NFSv4
"""

helps['netappfiles volume update'] = """
    type: command
    short-summary: Update the specified ANF volume with the values provided. Unspecified values will remain unchanged. Export policies are amended/created with the subgroup commands
    parameters:
        - name: --account-name -a
          short-summary: The name of the ANF account
        - name: --pool-name -p
          short-summary: The name of the ANF pool
        - name: --name --volume-name -n -v
          short-summary: The name of the ANF volume
        - name: --service-level
          short-summary: The service level
        - name: --usage-threshold
          short-summary: The maximum storage quota allowed for a file system as integer number of GiB. Min 100 GiB, max 100TiB"
        - name: --tags
          short-summary: Space-separated tags in `key[=value]` format
    examples:
        - name: Update an ANF volume
          text: >
            az netappfiles volume update -g mygroup --account-name myaccname --pool-name mypoolname --name myvolname --service-level ultra --usage-threshold 100 --tags mytag=specialvol
"""

helps['netappfiles volume delete'] = """
    type: command
    short-summary: Delete the specified ANF volume.
    parameters:
        - name: --account-name -a
          short-summary: The name of the ANF account
        - name: --pool-name -p
          short-summary: The name of the ANF pool
        - name: --name --volume-name -n -v
          short-summary: The name of the ANF volume
    examples:
        - name: Delete an ANF volume
          text: >
            az netappfiles volume delete -g mygroup --account-name myaccname --pool-name mypoolname --name myvolname
"""

helps['netappfiles volume list'] = """
    type: command
    short-summary: List the ANF Pools for the specified account.
    parameters:
        - name: --account-name -a
          short-summary: The name of the ANF account
        - name: --pool-name -p
          short-summary: The name of the ANF pool
    examples:
        - name: List the ANF volumes of the pool
          text: >
            az netappfiles volume list -g mygroup --account-name myaccname --pool-name mypoolname
"""

helps['netappfiles volume show'] = """
    type: command
    short-summary: Get the specified ANF volume.
    parameters:
        - name: --account-name -a
          short-summary: The name of the ANF account
        - name: --pool-name -p
          short-summary: The name of the ANF pool
        - name: --name --volume-name -n -v
          short-summary: The name of the ANF pool
    examples:
        - name: Returns the properties of the given ANF volume
          text: >
            az netappfiles volume show -g mygroup --account-name myaccname --pool-name mypoolname --name myvolname
"""

# volume subgroup to create export policy attribute

helps['netappfiles volume export-policy'] = """
    type: group
    short-summary: Manage Azure NetApp Files (ANF) Volume export policies.
"""

helps['netappfiles volume export-policy add'] = """
    type: command
    short-summary: Add a new rule to the export policy for a volume.
    parameters:
        - name: --account-name -a
          short-summary: The name of the ANF account
        - name: --pool-name -p
          short-summary: The name of the ANF pool
        - name: --name --volume-name -n -v
          short-summary: The name of the ANF volume
        - name: --rule-index
          short-summary: Order index. No number can be repeated. Max 6 rules.
        - name: --unix-read-only
          short-summary: Indication of read only access
        - name: --unix-read-write
          short-summary: Indication of read and write access
        - name: --cifs
          short-summary: Indication that CIFS protocol is allowed
        - name: --nfsv3
          short-summary: Indication that NFSv3 protocol is allowed
        - name: --nfsv4
          short-summary: Indication that NFSv4 protocol is allowed
        - name: --allowed-clients
          short-summary: Client ingress specification as comma separated string with IPv4 CIDRs, IPv4 host addresses and host names)
    examples:
        - name: Add an export policy rule for the ANF volume
          text: >
            az netappfiles volume export-policy add -g mygroup --account-name myaccname --pool-name mypoolname --name myvolname --allowed-clients "1.2.3.0/24" --rule-index 2 --unix-read-only true --unix-read-write false --cifs false --nfsv3 true --nfsv4 false
"""

helps['netappfiles volume export-policy list'] = """
    type: command
    short-summary: List the export policy rules for a volume.
    parameters:
        - name: --account-name -a
          short-summary: The name of the ANF account
        - name: --pool-name -p
          short-summary: The name of the ANF pool
        - name: --name --volume-name -n -v
          short-summary: The name of the ANF volume
    examples:
        - name: List the export policy rules for an ANF volume
          text: >
            az netappfiles volume export-policy list -g mygroup --account-name myaccname --pool-name mypoolname --name myvolname
"""

helps['netappfiles volume export-policy remove'] = """
    type: command
    short-summary: Remove a rule from the export policy for a volume by rule index. The current rules can be obtained by performing the subgroup list command.
    parameters:
        - name: --account-name -a
          short-summary: The name of the ANF account
        - name: --pool-name -p
          short-summary: The name of the ANF pool
        - name: --name --volume-name -n -v
          short-summary: The name of the ANF volume
        - name: --rule-index
          short-summary: Order index. Range 1 to 6.
    examples:
        - name: Remove an export policy rule for an ANF volume
          text: >
            az netappfiles volume export-policy remove -g mygroup --account-name myaccname --pool-name mypoolname --name myvolname --rule-index 4
"""

# mounttargets

helps['netappfiles list-mount-targets'] = """
    type: command
    short-summary: List the mount targets of an Azure NetApp Files (ANF) volume.
    parameters:
        - name: --account-name -a
          short-summary: The name of the ANF account
        - name: --pool-name -p
          short-summary: The name of the ANF pool
        - name: --volume-name -v
          short-summary: The name of the ANF pool
    examples:
        - name: list the mount targets of an ANF volume
          text: >
            az netappfiles list-mount-targets -g mygroup --account-name myaccname --pool-name mypoolname --volume-name myvolname
"""

# snapshots

helps['netappfiles snapshot'] = """
    type: group
    short-summary: Manage Azure NetApp Files (ANF) Snapshot Resources.
"""

helps['netappfiles snapshot create'] = """
    type: command
    short-summary: Create a new Azure NetApp Files (ANF) snapshot.
    parameters:
        - name: --account-name -a
          short-summary: The name of the ANF account
        - name: --pool-name -p
          short-summary: The name of the ANF pool
        - name: --volume-name -v
          short-summary: The name of the ANF volume
        - name: --name --snapshot-name -n -s
          short-summary: The name of the ANF snapshot
        - name: --file-system-id
          short-summary: The uuid of the volume
    examples:
        - name: Create an ANF snapshot
          text: >
            az netappfiles snapshot create -g mygroup --account-name myaccname --pool-name mypoolname --volume-name myvolname --name mysnapname -l eastus --file-system-id 13641da9-c0e9-4b97-84fc-4f8014a93848
"""

helps['netappfiles snapshot delete'] = """
    type: command
    short-summary: Delete the specified ANF snapshot.
    parameters:
        - name: --account-name -a
          short-summary: The name of the ANF account
        - name: --pool-name -p
          short-summary: The name of the ANF pool
        - name: --volume-name -v
          short-summary: The name of the ANF volume
        - name: --name --snapshot-name -n -s
          short-summary: The name of the ANF snapshot
    examples:
        - name: Delete an ANF snapshot
          text: >
            az netappfiles snapshot delete -g mygroup --account-name myaccname --pool-name mypoolname --volume-name myvolname --name mysnapname
"""

helps['netappfiles snapshot list'] = """
    type: command
    short-summary: List the snapshots of an ANF volume.
    parameters:
        - name: --account-name -a
          short-summary: The name of the ANF account
        - name: --pool-name -p
          short-summary: The name of the ANF pool
        - name: --volume-name -v
          short-summary: The name of the ANF volume
    examples:
        - name: list the snapshots of an ANF volume
          text: >
            az netappfiles snapshot list -g mygroup --account-name myaccname --pool-name mypoolname --volume-name myvolname
"""

helps['netappfiles snapshot show'] = """
    type: command
    short-summary: Get the specified ANF snapshot.
    parameters:
        - name: --account-name -a
          short-summary: The name of the ANF account
        - name: --pool-name -p
          short-summary: The name of the ANF pool
        - name: --volume-name -v
          short-summary: The name of the ANF volume
        - name: --name --snapshot-name -n -s
          short-summary: The name of the ANF snapshot
    examples:
        - name: Return the specified ANF snapshot
          text: >
            az netappfiles snapshot show -g mygroup --account-name myaccname --pool-name mypoolname --volume-name myvolname --name mysnapname
"""
