# 0x11. What happens when you type google.com in your browser and press Enter
Have you ever wondered what happens when you type a URL like “https://www.google.com" in your browser and press Enter? The process may seem seamless, but a series of intricate steps occur to deliver the desired webpage. In this blog post, we will unravel the journey of a web request, exploring concepts such as DNS requests, TCP/IP, firewalls, HTTPS/SSL, load-balancers, web servers, application servers, and databases.

DNS Request: Upon pressing Enter, the first step involves a DNS (Domain Name System) request. The browser extracts the domain name ‘www.google.com' from the URL and sends a DNS query to a DNS resolver or the ISP’s DNS servers. The resolver then searches for the IP address associated with the domain name. If found, it is returned to the browser; otherwise, the resolver queries other DNS servers until a valid IP address is obtained.
TCP/IP: With the IP address in hand, the browser initiates a TCP/IP (Transmission Control Protocol/Internet Protocol) connection. TCP breaks the data into packets and establishes a connection between the client (your browser) and the server (Google’s infrastructure). IP takes care of addressing and routing these packets over the internet.

Firewall: At this stage, the web request encounters firewalls, which act as a security barrier between the internet and the server. Firewalls examine the incoming traffic, filtering out potential threats and unauthorized access attempts. If the request passes through the firewall, it proceeds to the next step.

HTTPS/SSL: To ensure secure communication, HTTPS (Hypertext Transfer Protocol Secure) is employed. HTTPS relies on SSL (Secure Sockets Layer) or its successor, TLS (Transport Layer Security), to encrypt the data transmitted between the client and server. This encryption protects sensitive information from being intercepted or tampered with by malicious actors.

Load-Balancer: For popular websites like Google, a load-balancer distributes incoming requests across multiple servers to optimize performance and prevent overload. The load-balancer analyzes factors such as server availability, response time, and current load to determine the best server to handle each request. It ensures efficient utilization of resources and maintains the responsiveness of the website.

Web Server: The load-balancer forwards the request to an appropriate web server. The web server (e.g., Apache, Nginx) processes the request, retrieves the requested files or generates dynamic content based on the URL parameters, and sends back an HTTP response to the browser. It handles tasks such as serving static files, executing server-side scripts, and interacting with the application server.

Application Server: In cases where dynamic content is involved, the web server passes the request to an application server (e.g., Tomcat, Node.js). The application server executes the necessary business logic, interacts with databases, performs computations, and generates the final content to be sent back to the web server.
Database: If the request requires data retrieval or storage, the application server communicates with one or more databases to fetch or update information. Databases like MySQL, PostgreSQL, or NoSQL variants store, organize, and retrieve structured or unstructured data as requested by the application server.

# Conclusion:
The process of typing a URL and pressing Enter triggers a complex chain of events, involving DNS requests, TCP/IP connections, firewalls, HTTPS/SSL encryption, load-balancers, web servers, application servers, and databases. Each component plays a crucial role in delivering the desired web content efficiently and securely. Understanding this journey empowers us to appreciate the intricate workings of the internet and the robust infrastructure supporting it.




