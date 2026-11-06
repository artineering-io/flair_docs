---
title: "Licensing Server"
sidebar:
  order: 3
---
<span class="new-label">New in Flair 1.2</span>
A licensing server can be used to **_Relay_ Flair licenses through a local network**, floating the licenses between artists when needed. These licenses work well when artists need to **share licenses** or in **air-gapped or otherwise offline environments**.

:::note
Floating licenses are available when purchasing multiple Flair _STUDIO_ or _INDIE for Education_ licenses. [Get in touch](https://artineering.io/contact) with our sales team for more information on purchasing floating licenses.
:::

---

## License distribution

The Flair Relay licensing server distributes the available licenses to whichever _node_ claims it, be it an artist workstation or a computer in the farm in headless mode.

All Maya/Flair instances (sessions) opened on the same node share a claimed license. So if an artist has 5 Maya sessions open using Flair on their workstation, they are only using _one_ Flair license.

Licenses are claimed the moment the Flair plugin loads, so make sure to turn off `Auto load` within the _Plug-in Manager_ (`Windows -> Settings/Preferences -> Plug-in Manager -> flairEngine`) so that licenses are not automatically claimed even though they are not in use. The Flair plugin auto-loads whenever it is required by a node in the scene or a tool within the Flair Shelf.

Claimed licenses are released in two ways:
* Once the last instance of Flair in a node is closed by either unloading the plugin or closing Maya where the Flair plugin was loaded.
* The relay server doesn't receive a heartbeat from the node within 60 seconds.

Once released, the license is free to be claimed by a new node again.

---

## Setup
Once you **receive the Flair Relay files** from us, follow the steps below to setup the licensing server.

1. Make sure the server has a human-readable hostname or a static IP address within your network
2. **Extract** the `Flair Relay` files into a folder on the server machine.
3. **Open that folder within the Terminal** or PowerShell.
4. **Run** `./relay serve` to start the floating license sever.
5. (Optional) Relay will be served on port `6349` by default. To define a custom port, serve by specifying the port: `./relay serve --port ####`.
6. Open another Terminal/PowerShell in the same folder and run `./relay ls --plain` to check the status of the server.
    
<figure class="aio-ui aio-window">
<img src="/media/maya/setup/relay/relay_ls.png" alt="The available licenses are listed by running: ./relay ls" />
</figure>

---

### Adding firewall rules

Relay will need to be **permitted through the firewall** of the server machine for computers on the network **to connect to it**. Contact your network administrator so that they can configure the firewall for your environment.

Below are some basic instructions for Windows, macOS and Linux, but these may be quite different depending on how your environment is setup.

#### On Windows

**Add a program exception**

1. Go to Settings → Privacy and Security → Windows Security → `Firewall and Network Protection`
2. Click on `Advanced Settings`
3. Navigate to `Inbound Rules` and click on `New Rule...`
4. Select `Program` and click on `Next >`
5. Choose `This program path:` , `Browse...` to the folder where relay is located and double-click on `relay.exe`. Click on `Next >` to continue.
6. Choose `Allow the connection` and click on `Next >`
7. Select all the checkboxes that apply to the rule. Domain, Private, and Public and click on `Next >`
8. Specify a name for the rule e.g., `Flair Server` and click on `Finish` to complete the process

#### On macOS
Usually, a prompt will appear asking if you want the application "relay" to accept incoming network connections. When prompted, press on `Allow`.

If this does not occur, you can manually add an exception as follows:
1. Open the `Apple menu -> System Settings...`
2. Go to `Network -> Firewall` and click on `Options...`
3. At the bottom of the list on the left, click on the `+` button
4. Select the `relay` application from the folder where you have placed the Flair relay files

#### On Linux

1. Check what firewall zone your Linux server is operating in
    
    ```bash
    firewall-cmd --get-active-zones
    ```
    
2. (Optional) Change the zone your Linux server is operating in for your _interface_ (which you know from the previous command).
    
    ```bash
    sudo firewall-cmd --permanent --zone=work --change-interface=eth0
    ```
    
3. Run this command to **allow incoming traffic on the relay port** for your configured zone (work in this case)
    
    ```bash
    sudo firewall-cmd --permanent --zone=work --add-port=6349/tcp
    sudo firewall-cmd --reload
    ```

---

## Troubleshooting

### Test communication with Relay

Once the relay server is running, you can **check if it is reachable** with curl

#### On Windows (PowerShell)

```powershell
& curl.exe -v -X GET "http://SERVERNAME:PORT/v1/health"  ## HTTP/1.1 200 OK
```

#### On macOS and Linux

```bash
curl -v -X GET "http://SERVERNAME:PORT/v1/health"  ## HTTP/1.1 200 OK
```

If host cannot be reached, check your [firewall configuration](#adding-firewall-rules) and enable the necessary ports.

### Setting a hostname

#### On Windows

1. Open **Settings** (`Win + I`)
2. Go to **System > About**
3. Click **Rename this PC**
4. Enter a new name and restart your computer

#### On macOS
1. Open the `Apple menu -> System Settings...`
2. Go to `General -> Sharing`
3. Under Local hostname click on `Edit...`
4. Enter a new name and restart your computer

#### On Linux (RHEL 7+)

Run the following command where `NEW-HOSTNAME` is the new hostname of the server 

```bash
sudo hostnamectl set-hostname NEW-HOSTNAME
```
