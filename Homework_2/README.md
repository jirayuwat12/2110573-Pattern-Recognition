# MLE

given
$y_2 =\alpha y_1+\omega _1$ and
$y_1 =\alpha y_0+\omega _0$

where $\omega _0$ and $\omega _1$ are independent and identically distributed (i.i.d.) Gaussian random variables with mean 0 and variance $\sigma ^2$.

and $y_0$ is Gaussian random variable with mean 0 and variance $\lambda$.

which we know only $\lambda$ and $\sigma ^2$.

## T1 - Find the MLE of $\alpha$.

$$
\begin{align*}
p(y_0) &= \frac{1}{\sqrt{2\pi\lambda}}e^{-\frac{y_0^2}{2\lambda}}\\
p(y_1|y_0) &= \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(y_1-\alpha y_0)^2}{2\sigma^2}}\\
p(y_2|y_1) &= \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(y_2-\alpha y_1)^2}{2\sigma^2}}\\

L(\alpha) &= p(y_2|y_1)p(y_1|y_0)p(y_0)\\
&= \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(y_2-\alpha y_1)^2}{2\sigma^2}}\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(y_1-\alpha y_0)^2}{2\sigma^2}}\frac{1}{\sqrt{2\pi\lambda}}e^{-\frac{y_0^2}{2\lambda}}\\
\ln L(\alpha) &= \ln \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(y_2-\alpha y_1)^2}{2\sigma^2}} + \ln \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(y_1-\alpha y_0)^2}{2\sigma^2}} + \ln \frac{1}{\sqrt{2\pi\lambda}}e^{-\frac{y_0^2}{2\lambda}}\\
&= \ln \frac{1}{\sqrt{2\pi\sigma^2}} -\frac{(y_2-\alpha y_1)^2}{2\sigma^2} + \ln \frac{1}{\sqrt{2\pi\sigma^2}} -\frac{(y_1-\alpha y_0)^2}{2\sigma^2} + \ln \frac{1}{\sqrt{2\pi\lambda}} -\frac{y_0^2}{2\lambda}\\
&= \ln \frac{1}{\sqrt{2\pi\sigma^2}} -\frac{y_2^2-2\alpha y_1y_2+\alpha^2y_1^2}{2\sigma^2} + \ln \frac{1}{\sqrt{2\pi\sigma^2}} -\frac{y_1^2-2\alpha y_0y_1+\alpha^2y_0^2}{2\sigma^2} + \ln \frac{1}{\sqrt{2\pi\lambda}} -\frac{y_0^2}{2\lambda}\\
&= \ln \frac{1}{\sqrt{2\pi\sigma^2}} -\frac{y_2^2}{2\sigma^2} + \frac{\alpha y_1y_2}{\sigma^2} -\frac{\alpha^2y_1^2}{2\sigma^2} + \ln \frac{1}{\sqrt{2\pi\sigma^2}} -\frac{y_1^2}{2\sigma^2} + \frac{\alpha y_0y_1}{\sigma^2} -\frac{\alpha^2y_0^2}{2\sigma^2} + \ln \frac{1}{\sqrt{2\pi\lambda}} -\frac{y_0^2}{2\lambda}\\
\frac{\partial \ln L(\alpha)}{\partial \alpha} &= \frac{y_1y_2}{\sigma^2} -\frac{\alpha y_1^2}{\sigma^2} + \frac{y_0y_1}{\sigma^2} -\frac{\alpha y_0^2}{\sigma^2}\\
0 &= \frac{y_1y_2}{\sigma^2} -\frac{\alpha y_1^2}{\sigma^2} + \frac{y_0y_1}{\sigma^2} -\frac{\alpha y_0^2}{\sigma^2}\\
\frac{\alpha y_1^2}{\sigma^2} + \frac{\alpha y_0^2}{\sigma^2} &= \frac{y_1y_2}{\sigma^2} + \frac{y_0y_1}{\sigma^2}\\
\alpha y_1^2 + \alpha y_0^2 &= y_1y_2 + y_0y_1\\
\alpha (y_1^2 + y_0^2) &= y_1y_2 + y_0y_1\\
\alpha &= \frac{y_1y_2 + y_0y_1}{y_1^2 + y_0^2}
\end{align*}
$$