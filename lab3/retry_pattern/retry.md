# Retry pattern
## What it is
The retry pattern is an architectural design pattern which handles transient failures when trying to access a service or network via retrying the failed operation. <br>
There are many different strategies on how to handle the retrying policies. For example, instantly retrying, having a delay before retrying, or flat out cancelling the operation. Although delay times and attempts differ from service to service, on occasions services might have documentation detailing the recommended retry policies for the specific service.
## What it solves
This strategy provides resilience to transient failures of distributed systems such as temporary connectivity loss, temporary service outages, or time outs on busy services. It will help recover from malfunctions that could be fixed by themselves.
## Limitations
This strategy can add latency on the client side from delays between tries. It will be counterproductive on long term issues. Is advised to set strategies according to the error codes received, while an error code 408 or 505 might change on a second or third attempt, errors like 400 will keep happening regardless of the iteration.
