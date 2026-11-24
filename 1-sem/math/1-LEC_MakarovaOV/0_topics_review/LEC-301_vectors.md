---
title: LEC-301 векторы
date: 2026-11-22
tags:
  - author/the-nataraja
---

# 3.1. Векторы

## Скалярные и векторные величины. Понятие вектора

При описании физических и геометрических задач величины делятся на два класса. Одни величины — например, масса, температура, площадь или время — полностью задаются одним действительным числом (после выбора единицы измерения). Такие величины называют **скалярными** (или просто **скалярами**).

Другие величины — например, перемещение тела, скорость, ускорение или сила — невозможно задать одним числом: помимо числового значения, для них необходимо указать **направление** в пространстве. Такие величины называют **векторными**. Чтобы работать с ними математически, вводят геометрическую модель — вектор.

Отрезок, у которого одна из граничных точек выбрана **началом**, а вторая — **концом**, называют **направленным отрезком**. Направление на нём указывают стрелкой от начала к концу. Направленный отрезок с началом $A$ и концом $B$ обозначают $\overrightarrow{AB}$, а произвольный вектор в формулах — строчной буквой со стрелкой ($\vec{a}, \vec{b}, \vec{c}$).

Часто рассматривают ситуацию, когда две точки испытывают одинаковое перемещение в одном и том же направлении и на одно и то же расстояние — например, при поступательном движении твёрдого тела. С геометрической точки зрения это разные направленные отрезки, но описывают они одно и то же смещение. Чтобы объединить все такие направленные отрезки в один объект, понятие вектора отделяют от конкретной точки приложения.

Два ненулевых направленных отрезка $\overrightarrow{AB}$ и $\overrightarrow{CD}$ называют **сонаправленными** (обозначение $\overrightarrow{AB} \uparrow\uparrow \overrightarrow{CD}$), если они лежат на одной прямой или на параллельных прямых и лучи $AB$ и $CD$ направлены в одну сторону. Два направленных отрезка называют **равными**, если они сонаправлены и имеют одинаковые длины.

> **Вектор (свободный вектор)** — это геометрический объект, характеризуемый длиной и направлением; любые два равных (сонаправленных и одинаковых по длине) направленных отрезка представляют один и тот же вектор.

Из этого определения следует, что вектор можно переносить параллельно самому себе в любую точку пространства — от этого он не меняется. Поэтому начало вектора можно совместить с любой удобной точкой, «отложив» его от неё.

<svg viewBox="0 0 480 150" style="max-width: 520px; width: 100%; height: auto; display: block; margin: 1em auto;">
  <defs>
    <marker id="v1-blue" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#3b82f6"/>
    </marker>
    <marker id="v1-red" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#ef4444"/>
    </marker>
  </defs>
  <line x1="40" y1="105" x2="180" y2="125" stroke="currentColor" stroke-opacity="0.28" stroke-dasharray="4 4" stroke-width="1.2"/>
  <line x1="160" y1="45" x2="300" y2="65" stroke="currentColor" stroke-opacity="0.28" stroke-dasharray="4 4" stroke-width="1.2"/>
  <line x1="40" y1="105" x2="160" y2="45" stroke="#3b82f6" stroke-width="2.5" marker-end="url(#v1-blue)"/>
  <circle cx="40" cy="105" r="3" fill="#3b82f6"/>
  <text x="26" y="116" fill="currentColor" font-size="13" font-family="sans-serif">A</text>
  <text x="163" y="42" fill="currentColor" font-size="13" font-family="sans-serif">B</text>
  <text x="90" y="65" fill="#3b82f6" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">a</text>
  <line x1="180" y1="125" x2="300" y2="65" stroke="#3b82f6" stroke-width="2.5" marker-end="url(#v1-blue)"/>
  <circle cx="180" cy="125" r="3" fill="#3b82f6"/>
  <text x="166" y="136" fill="currentColor" font-size="13" font-family="sans-serif">C</text>
  <text x="303" y="62" fill="currentColor" font-size="13" font-family="sans-serif">D</text>
  <text x="230" y="85" fill="#3b82f6" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">a</text>
  <line x1="450" y1="45" x2="330" y2="105" stroke="#ef4444" stroke-width="2.5" marker-end="url(#v1-red)"/>
  <circle cx="450" cy="45" r="3" fill="#ef4444"/>
  <text x="454" y="43" fill="currentColor" font-size="13" font-family="sans-serif">E</text>
  <text x="316" y="116" fill="currentColor" font-size="13" font-family="sans-serif">F</text>
  <text x="394" y="92" fill="#ef4444" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">−a</text>
</svg>

*Равные направленные отрезки $\overrightarrow{AB} = \overrightarrow{CD}$ задают один и тот же вектор $\vec{a}$, а отрезок $\overrightarrow{EF}$ той же длины, но противоположного направления задаёт вектор $-\vec{a}$.*

> [!NOTE] Свободные, скользящие и связанные векторы
> В курсе высшей математики по умолчанию рассматриваются именно **свободные векторы** — они не привязаны к точке пространства. В механике и физике иногда используют более строгие модели: **скользящие векторы** (их можно сдвигать только вдоль линии действия, например силу, приложенную к твёрдому телу) и **связанные векторы** (точка начала фиксирована, например скорость конкретной точки в потоке жидкости). В пределах этой главы все векторы свободны, если явно не указана точка приложения.

---

## Характеристики и особые виды векторов

Чтобы описывать векторы и выполнять над ними действия, вводят их базовую числовую меру — длину — и несколько выделенных типов векторов.

> **Длина (или модуль) вектора $\vec{a}$** — неотрицательное число, равное длине любого изображающего его направленного отрезка; обозначается $|\vec{a}|$ (или $|\overrightarrow{AB}| = AB$).

*(В линейной алгебре и анализе длину вектора также часто называют **нормой** и обозначают двойными вертикальными чертами $\|\vec{a}\|$.)*

Рассмотрим четыре особых вида векторов:

1. **Нулевой вектор ($\vec{0}$)** — вектор, начало и конец которого совпадают (например, $\overrightarrow{AA}$ или $\overrightarrow{BB}$).
   Длина нулевого вектора равна нулю: $|\vec{0}| = 0$. Наоборот, если длина вектора равна нулю, то этот вектор — нулевой. Направление нулевого вектора **не определено** (условно его можно считать направленным в любую сторону).
2. **Вектор, противоположный данному ($-\vec{a}$)** — вектор, имеющий ту же длину, что и $\vec{a}$, но противоположное направление.
   Если $\vec{a} = \overrightarrow{AB}$, то $-\vec{a} = \overrightarrow{BA}$. Для нулевого вектора противоположный совпадает с ним самим: $-\vec{0} = \vec{0}$.
3. **Единичный вектор** — любой вектор, длина которого равна единице ($|\vec{e}| = 1$).
4. **Орт вектора $\vec{a}$** (обозначается $\vec{a}^{\,0}$) — единичный вектор, сонаправленный с данным ненулевым вектором $\vec{a}$:

   $$
   |\vec{a}^{\,0}| = 1 \quad \text{и} \quad \vec{a}^{\,0} \uparrow\uparrow \vec{a}.
   $$

   Орт показывает «чистое направление» вектора $\vec{a}$, очищенное от его длины.

> [!NOTE] Ловушка с нулевым вектором и ортом
> Нулевой вектор $\vec{0}$ **не имеет орта**. Причина в том, что у $\vec{0}$ нет определённого направления, поэтому невозможно выбрать конкретный единичный вектор, «сонаправленный с ним». Позже, когда орт будет выражаться через деление вектора на его длину, невозможность орта для $\vec{0}$ проявится и алгебраически — как запрет деления на $|\vec{0}| = 0$.

---

## Коллинеарные и компланарные векторы

Когда в задаче участвуют сразу несколько векторов, важно уметь описывать их взаимное расположение на прямой и на плоскости.

> **Коллинеарные векторы** — векторы, которые лежат на одной прямой или на параллельных прямых (обозначение: $\vec{a} \parallel \vec{b}$).

Поскольку свободные векторы можно отложить от одной точки, коллинеарность означает, что при совмещении начал такие векторы ложатся на одну прямую. Для ненулевых коллинеарных векторов возможны два варианта направления:
* векторы направлены в одну сторону — они **сонаправлены** ($\vec{a} \uparrow\uparrow \vec{b}$);
* векторы направлены в противоположные стороны — они **противоположно направленны** ($\vec{a} \uparrow\downarrow \vec{b}$).

> [!NOTE] Нулевой вектор и нарушение транзитивности коллинеарности
> **Нулевой вектор $\vec{0}$ считается коллинеарным любому вектору.** В частности, у него можно при желании выбрать направление вдоль прямой любого заданного вектора.
>
> Это удобное соглашение имеет важную тонкость: на множестве всех векторов отношение коллинеарности **не транзитивно**. Например, два перпендикулярных ненулевых вектора $\vec{a}$ и $\vec{b}$ по отдельности коллинеарны нулевому вектору ($\vec{a} \parallel \vec{0}$ и $\vec{0} \parallel \vec{b}$), но между собой не коллинеарны ($\vec{a} \nparallel \vec{b}$). Для *ненулевых* векторов транзитивность выполняется.

В трёхмерном пространстве одного лишь понятия коллинеарности недостаточно — появляется аналогичное условие принадлежности общей плоскости.

> **Компланарные векторы** — векторы, которые параллельны некоторой общей плоскости (или, что то же самое, при приведении к общему началу лежат в одной плоскости).

Из этого определения вытекают два полезных факта:
* **Любые два вектора всегда компланарны.** Если отложить два ненулевых неколлинеарных вектора от общей точки $O$, через две пересекающиеся прямые всегда проходит ровно одна плоскость. Если же векторы коллинеарны (или хотя бы один из них нулевой), через одну прямую проходит бесконечно много плоскостей.
* **Три вектора заведомо компланарны**, если хотя бы один из них нулевой или хотя бы два из них коллинеарны. В общем случае (когда среди трёх векторов нет нулевых и нет коллинеарных пар) они могут как лежать в одной плоскости, так и не быть компланарными.

<svg viewBox="0 0 520 170" style="max-width: 560px; width: 100%; height: auto; display: block; margin: 1em auto;">
  <defs>
    <marker id="v2-blue" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#3b82f6"/>
    </marker>
    <marker id="v2-green" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#10b981"/>
    </marker>
    <marker id="v2-red" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#ef4444"/>
    </marker>
    <marker id="v2-amber" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#f59e0b"/>
    </marker>
  </defs>
  <line x1="25" y1="50" x2="125" y2="30" stroke="#3b82f6" stroke-width="2.4" marker-end="url(#v2-blue)"/>
  <text x="68" y="29" fill="#3b82f6" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">a</text>
  <line x1="35" y1="90" x2="185" y2="60" stroke="#10b981" stroke-width="2.4" marker-end="url(#v2-green)"/>
  <text x="108" y="65" fill="#10b981" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">b</text>
  <line x1="175" y1="112" x2="75" y2="132" stroke="#f59e0b" stroke-width="2.4" marker-end="url(#v2-amber)"/>
  <text x="122" y="140" fill="#f59e0b" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">c</text>
  <line x1="205" y1="140" x2="235" y2="45" stroke="#ef4444" stroke-width="2.4" marker-end="url(#v2-red)"/>
  <text x="230" y="96" fill="#ef4444" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">d</text>
  <line x1="265" y1="15" x2="265" y2="155" stroke="currentColor" stroke-opacity="0.22" stroke-width="1.2"/>
  <polygon points="295,140 460,140 500,82 335,82" fill="currentColor" fill-opacity="0.08" stroke="currentColor" stroke-opacity="0.35" stroke-width="1.2"/>
  <line x1="335" y1="122" x2="430" y2="122" stroke="#3b82f6" stroke-width="2.4" marker-end="url(#v2-blue)"/>
  <text x="380" y="136" fill="#3b82f6" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">u</text>
  <line x1="335" y1="122" x2="380" y2="90" stroke="#10b981" stroke-width="2.4" marker-end="url(#v2-green)"/>
  <text x="342" y="102" fill="#10b981" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">v</text>
  <circle cx="335" cy="122" r="2.8" fill="currentColor"/>
  <line x1="418" y1="108" x2="425" y2="24" stroke="#ef4444" stroke-width="2.4" marker-end="url(#v2-red)"/>
  <circle cx="418" cy="108" r="2.8" fill="#ef4444"/>
  <text x="430" y="55" fill="#ef4444" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">w</text>
</svg>

*Слева: векторы $\vec{a}, \vec{b}, \vec{c}$ коллинеарны ($\vec{a} \uparrow\uparrow \vec{b}$, $\vec{a} \uparrow\downarrow \vec{c}$), а вектор $\vec{d}$ им не коллинеарен. Справа: векторы $\vec{u}$ и $\vec{v}$ лежат в плоскости, а вектор $\vec{w}$ выходит из неё, поэтому тройка $\vec{u}, \vec{v}, \vec{w}$ не компланарна.*

---

## Линейные операции над векторами

Над векторами вводят две основные операции: **сложение** двух векторов и **умножение** вектора на действительное число. Их называют **линейными операциями** над векторами.

### Сложение и вычитание векторов

Сложение геометрических векторов моделирует последовательное перемещение: если сначала сдвинуться на вектор $\vec{a}$, а затем из новой точки сдвинуться на вектор $\vec{b}$, итоговое перемещение от начальной точки к конечной и есть сумма $\vec{a} + \vec{b}$.

> **Сумма векторов $\vec{a} + \vec{b}$ (правило треугольника)** — вектор $\overrightarrow{AC}$, полученный в том случае, если от конца вектора $\vec{a} = \overrightarrow{AB}$ отложить вектор $\vec{b} = \overrightarrow{BC}$, а затем соединить начало первого с концом второго.

Правило треугольника работает **всегда**, в том числе для коллинеарных векторов (тогда «треугольник» вырождается в отрезок на одной прямой) и для нулевого вектора.

Для неколлинеарных векторов существует эквивалентное **правило параллелограмма**: если отложить $\vec{a}$ и $\vec{b}$ от общего начала $O$ и достроить на них параллелограмм, то диагональ, выходящая из той же точки $O$, изображает сумму $\vec{a} + \vec{b}$. Противоположная сторона параллелограмма равна и сонаправлена вектору $\vec{b}$, поэтому оба правила дают один и тот же вектор.

При сложении трёх и более векторов правило треугольника повторяют по цепочке: каждый следующий вектор откладывают от конца предыдущего, а сумма соединяет начало самого первого с концом самого последнего (**правило многоугольника**). Если ломаная замкнулась (конец последнего вектора совпал с началом первого), сумма всех векторов равна $\vec{0}$.

**Разность векторов $\vec{a} - \vec{b}$** определяют через уже введённые понятия суммы и противоположного вектора:

$$
\vec{a} - \vec{b} = \vec{a} + (-\vec{b}).
$$

На рисунке с общим началом $O$ ($\vec{a} = \overrightarrow{OA}$, $\vec{b} = \overrightarrow{OB}$) разность $\vec{a} - \vec{b}$ соответствует второй диагонали параллелограмма — вектору $\overrightarrow{BA}$, направленному **от конца вычитаемого $\vec{b}$ к концу уменьшаемого $\vec{a}$**. Действительно, по правилу треугольника $\overrightarrow{OB} + \overrightarrow{BA} = \overrightarrow{OA}$, то есть $\vec{b} + \overrightarrow{BA} = \vec{a}$, откуда $\overrightarrow{BA} = \vec{a} - \vec{b}$.

<svg viewBox="0 0 540 165" style="max-width: 580px; width: 100%; height: auto; display: block; margin: 1em auto;">
  <defs>
    <marker id="v3-blue" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#3b82f6"/>
    </marker>
    <marker id="v3-green" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#10b981"/>
    </marker>
    <marker id="v3-red" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#ef4444"/>
    </marker>
    <marker id="v3-amber" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#f59e0b"/>
    </marker>
  </defs>
  <line x1="25" y1="130" x2="120" y2="130" stroke="#3b82f6" stroke-width="2.4" marker-end="url(#v3-blue)"/>
  <text x="68" y="146" fill="#3b82f6" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">a</text>
  <line x1="120" y1="130" x2="160" y2="42" stroke="#10b981" stroke-width="2.4" marker-end="url(#v3-green)"/>
  <text x="148" y="92" fill="#10b981" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">b</text>
  <line x1="25" y1="130" x2="160" y2="42" stroke="#ef4444" stroke-width="2.6" marker-end="url(#v3-red)"/>
  <text x="62" y="75" fill="#ef4444" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">a + b</text>
  <circle cx="25" cy="130" r="2.8" fill="currentColor"/>
  <line x1="205" y1="130" x2="300" y2="130" stroke="#3b82f6" stroke-width="2.4" marker-end="url(#v3-blue)"/>
  <text x="248" y="146" fill="#3b82f6" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">a</text>
  <line x1="205" y1="130" x2="245" y2="42" stroke="#10b981" stroke-width="2.4" marker-end="url(#v3-green)"/>
  <text x="208" y="84" fill="#10b981" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">b</text>
  <line x1="300" y1="130" x2="340" y2="42" stroke="currentColor" stroke-opacity="0.35" stroke-dasharray="4 4" stroke-width="1.4"/>
  <line x1="245" y1="42" x2="340" y2="42" stroke="currentColor" stroke-opacity="0.35" stroke-dasharray="4 4" stroke-width="1.4"/>
  <line x1="205" y1="130" x2="340" y2="42" stroke="#ef4444" stroke-width="2.6" marker-end="url(#v3-red)"/>
  <text x="278" y="78" fill="#ef4444" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">a + b</text>
  <circle cx="205" cy="130" r="2.8" fill="currentColor"/>
  <line x1="385" y1="130" x2="480" y2="130" stroke="#3b82f6" stroke-width="2.4" marker-end="url(#v3-blue)"/>
  <text x="428" y="146" fill="#3b82f6" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">a</text>
  <line x1="385" y1="130" x2="425" y2="42" stroke="#10b981" stroke-width="2.4" marker-end="url(#v3-green)"/>
  <text x="388" y="84" fill="#10b981" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">b</text>
  <line x1="425" y1="42" x2="480" y2="130" stroke="#f59e0b" stroke-width="2.6" marker-end="url(#v3-amber)"/>
  <text x="462" y="84" fill="#f59e0b" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">a − b</text>
  <circle cx="385" cy="130" r="2.8" fill="currentColor"/>
</svg>

*Слева: правило треугольника. В центре: правило параллелограмма. Справа: вычитание $\vec{a} - \vec{b}$ (стрелка разности направлена от конца вычитаемого к концу уменьшаемого).*

### Умножение вектора на число

> **Произведение вектора $\vec{a}$ на действительное число $\lambda \in \mathbb{R}$** (обозначается $\lambda \vec{a}$) — это вектор, длина которого равна $|\lambda| \cdot |\vec{a}|$, а направление устроено так:
> * при $\lambda > 0$ вектор $\lambda \vec{a}$ сонаправлен с $\vec{a}$ ($\lambda \vec{a} \uparrow\uparrow \vec{a}$);
> * при $\lambda < 0$ вектор $\lambda \vec{a}$ противоположно направлен с $\vec{a}$ ($\lambda \vec{a} \uparrow\downarrow \vec{a}$);
> * при $\lambda = 0$ или $\vec{a} = \vec{0}$ произведение равно нулевому вектору: $0 \cdot \vec{a} = \vec{0}$ и $\lambda \cdot \vec{0} = \vec{0}$.

Операция $\lambda\vec{a}$ геометрически означает растяжение (при $|\lambda| > 1$) или сжатие (при $|\lambda| < 1$) вектора вдоль его прямой, с разворотом на $180^\circ$ при отрицательном множителе.

<svg viewBox="0 0 500 135" style="max-width: 540px; width: 100%; height: auto; display: block; margin: 1em auto;">
  <defs>
    <marker id="v4-blue" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#3b82f6"/>
    </marker>
    <marker id="v4-green" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#10b981"/>
    </marker>
    <marker id="v4-red" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#ef4444"/>
    </marker>
    <marker id="v4-amber" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#f59e0b"/>
    </marker>
  </defs>
  <line x1="25" y1="45" x2="105" y2="25" stroke="#3b82f6" stroke-width="2.5" marker-end="url(#v4-blue)"/>
  <text x="60" y="25" fill="#3b82f6" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">a</text>
  <line x1="25" y1="112" x2="185" y2="72" stroke="#10b981" stroke-width="2.5" marker-end="url(#v4-green)"/>
  <text x="98" y="82" fill="#10b981" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">2a</text>
  <line x1="220" y1="42" x2="260" y2="32" stroke="#3b82f6" stroke-width="2.5" marker-end="url(#v4-blue)"/>
  <text x="225" y="24" fill="#3b82f6" font-size="13" font-weight="bold" font-style="italic" font-family="sans-serif">0.5a</text>
  <line x1="355" y1="78" x2="235" y2="108" stroke="#ef4444" stroke-width="2.5" marker-end="url(#v4-red)"/>
  <text x="285" y="114" fill="#ef4444" font-size="13" font-weight="bold" font-style="italic" font-family="sans-serif">−1.5a</text>
  <line x1="405" y1="68" x2="437" y2="60" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#v4-amber)"/>
  <text x="415" y="50" fill="#f59e0b" font-size="13" font-weight="bold" font-style="italic" font-family="sans-serif">a⁰</text>
</svg>

*Масштабирование вектора $\vec{a}$ и его орт $\vec{a}^{\,0}$ единичной длины.*

Умножение на число сразу связывает воедино несколько прежних понятий:

1. **Противоположный вектор:** $-\vec{a} = (-1)\vec{a}$ (при $\lambda = -1$ длина сохраняется, а направление меняется на противоположное).
2. **Формула орта (нормировка вектора):** для любого ненулевого вектора $\vec{a} \neq \vec{0}$ его орт получается делением вектора на его длину, то есть умножением на положительное число $\lambda = \frac{1}{|\vec{a}|}$:

   $$
   \vec{a}^{\,0} = \frac{1}{|\vec{a}|}\vec{a} = \frac{\vec{a}}{|\vec{a}|}.
   $$

   Проверка очевидна: множитель $\frac{1}{|\vec{a}|} > 0$ сохраняет направление $\vec{a}$, а длина результата равна $\frac{1}{|\vec{a}|} \cdot |\vec{a}| = 1$. Например, если $|\vec{a}| = 5$, то $\vec{a}^{\,0} = \frac{1}{5}\vec{a}$ (и обратно, $\vec{a} = |\vec{a}| \cdot \vec{a}^{\,0}$).
3. **Алгебраический критерий коллинеарности:** параллельность векторов теперь выражается уравнением.

> [!IMPORTANT] Теорема (критерий коллинеарности векторов)
> Пусть $\vec{a} \neq \vec{0}$. Вектор $\vec{b}$ коллинеарен вектору $\vec{a}$ **тогда и только тогда**, когда существует (причём единственное) действительное число $\lambda \in \mathbb{R}$, такое что:
>
> $$
> \vec{b} = \lambda \vec{a}.
> $$

**Доказательство:**
* ($\Leftarrow$) Если $\vec{b} = \lambda\vec{a}$, то при $\lambda = 0$ получаем $\vec{b} = \vec{0}$, который коллинеарен $\vec{a}$ по определению. При $\lambda \neq 0$ вектор $\lambda\vec{a}$ по определению сонаправлен или противоположно направлен с $\vec{a}$, значит лежит на той же или параллельной прямой: $\vec{b} \parallel \vec{a}$.
* ($\Rightarrow$) Пусть $\vec{b} \parallel \vec{a}$ и $\vec{a} \neq \vec{0}$.
  * Если $\vec{b} = \vec{0}$, подходит $\lambda = 0$: $0 \cdot \vec{a} = \vec{0}$.
  * Если $\vec{b} \neq \vec{0}$ и $\vec{b} \uparrow\uparrow \vec{a}$, положим $\lambda = \frac{|\vec{b}|}{|\vec{a}|} > 0$. Тогда вектор $\lambda\vec{a}$ сонаправлен с $\vec{a}$ (а значит и с $\vec{b}$) и имеет длину $\frac{|\vec{b}|}{|\vec{a}|}|\vec{a}| = |\vec{b}|$, откуда $\lambda\vec{a} = \vec{b}$.
  * Если $\vec{b} \neq \vec{0}$ и $\vec{b} \uparrow\downarrow \vec{a}$, положим $\lambda = -\frac{|\vec{b}|}{|\vec{a}|} < 0$. Вектор $\lambda\vec{a}$ противоположен по направлению вектору $\vec{a}$ (значит, сонаправлен с $\vec{b}$) и имеет длину $\left|-\frac{|\vec{b}|}{|\vec{a}|}\right||\vec{a}| = |\vec{b}|$, поэтому снова $\lambda\vec{a} = \vec{b}$.
* *Единственность $\lambda$:* если $\lambda_1\vec{a} = \lambda_2\vec{a}$, то, перенеся всё в одну часть и заметив по определению ниже, что $(\lambda_1 - \lambda_2)\vec{a} = \vec{0}$, по длине получаем $|\lambda_1 - \lambda_2| \cdot |\vec{a}| = 0$. Так как $|\vec{a}| \neq 0$, отсюда $\lambda_1 = \lambda_2$. $\blacksquare$

*(Условие $\vec{a} \neq \vec{0}$ в теореме существенно: если $\vec{a} = \vec{0}$ и $\vec{b} \neq \vec{0}$, векторы коллинеарны по соглашению, но равенство $\vec{b} = \lambda\vec{0} = \vec{0}$ не выполняется ни при каком $\lambda$. Более симметричная формулировка, охватывающая все случаи без исключений, звучит так: векторы $\vec{a}$ и $\vec{b}$ коллинеарны тогда и только тогда, когда найдутся числа $\alpha, \beta \in \mathbb{R}$, не равные нулю одновременно, для которых $\alpha\vec{a} + \beta\vec{b} = \vec{0}$.)*

### Свойства сложения векторов и их умножения на числа

Линейные операции над векторами подчиняются восьми базовым законам, аналогичным привычным правилам арифметики чисел. Именно эти восемь свойств позволяют раскрывать скобки, приводить подобные слагаемые и переносить слагаемые из одной части векторного равенства в другую.

Для любых векторов $\vec{a}, \vec{b}, \vec{c}$ и любых действительных чисел $\lambda, \mu \in \mathbb{R}$ выполняются равенства:

1. **Переместительность сложения** *(коммутативность)*: $\vec{a} + \vec{b} = \vec{b} + \vec{a}$.
2. **Сочетательность сложения** *(ассоциативность)*: $(\vec{a} + \vec{b}) + \vec{c} = \vec{a} + (\vec{b} + \vec{c})$.
3. **Роль нулевого вектора**: $\vec{a} + \vec{0} = \vec{a}$.
4. **Роль противоположного вектора**: $\vec{a} + (-\vec{a}) = \vec{0}$.
5. **Сочетательность умножения на число**: $\lambda(\mu\vec{a}) = (\lambda\mu)\vec{a}$.
6. **Распределительность по сложению чисел** *(дистрибутивность)*: $(\lambda + \mu)\vec{a} = \lambda\vec{a} + \mu\vec{a}$.
7. **Распределительность по сложению векторов** *(дистрибутивность)*: $\lambda(\vec{a} + \vec{b}) = \lambda\vec{a} + \lambda\vec{b}$.
8. **Умножение на единицу**: $1 \cdot \vec{a} = \vec{a}$.

Эти свойства позволяют упрощать векторные выражения точно так же, как алгебраические. Например:

$$
2(\vec{a} + 3\vec{b}) - (5\vec{a} - \vec{b}) = 2\vec{a} + 6\vec{b} - 5\vec{a} + \vec{b} = -3\vec{a} + 7\vec{b}.
$$

> [!abstract]- Доказательства основных свойств линейных операций
> Свойства 3, 4 и 8 следуют напрямую из определений $\vec{0}$, $-\vec{a}$ и умножения на $\lambda = 1$. Ниже разобраны доказательства остальных пяти свойств.
>
> * **Свойство 1 (коммутативность сложения).** Для неколлинеарных векторов обе суммы $\vec{a} + \vec{b}$ и $\vec{b} + \vec{a}$ изображаются одной и той же диагональю параллелограмма, построенного на $\vec{a}$ и $\vec{b}$ (разные лишь треугольники, на которые эта диагональ делит параллелограмм). Если один из векторов нулевой, равенство $\vec{a} + \vec{0} = \vec{0} + \vec{a} = \vec{a}$ очевидно. Если же оба вектора ненулевые и коллинеарны, проверка сводится к координатной прямой с выбором оси вдоль $\vec{a}$, где векторное сложение совпадает со сложением действительных чисел.
>
> * **Свойство 2 (ассоциативность сложения).** Отложим от произвольной точки $O$ последовательную цепочку векторов: $\overrightarrow{OA} = \vec{a}$, $\overrightarrow{AB} = \vec{b}$, $\overrightarrow{BC} = \vec{c}$.
>   По правилу треугольника:
>
>   $$
>   (\vec{a} + \vec{b}) + \vec{c} = (\overrightarrow{OA} + \overrightarrow{AB}) + \overrightarrow{BC} = \overrightarrow{OB} + \overrightarrow{BC} = \overrightarrow{OC}.
>   $$
>
>   С другой стороны, группируя два последних вектора:
>
>   $$
>   \vec{a} + (\vec{b} + \vec{c}) = \overrightarrow{OA} + (\overrightarrow{AB} + \overrightarrow{BC}) = \overrightarrow{OA} + \overrightarrow{AC} = \overrightarrow{OC}.
>   $$
>
>   Обе части равенства дают один и тот же вектор $\overrightarrow{OC}$ (рассуждение работает без исключений, даже если какие-то из точек $O, A, B, C$ совпадают или лежат на одной прямой).
>
> * **Свойство 5 (ассоциативность умножения на число).** Если $\lambda = 0$, $\mu = 0$ или $\vec{a} = \vec{0}$, обе части равны $\vec{0}$. Если все величины ненулевые, длины левого и правого векторов совпадают:
>
>   $$
>   |\lambda(\mu\vec{a})| = |\lambda| \cdot |\mu\vec{a}| = |\lambda| \cdot |\mu| \cdot |\vec{a}| = |\lambda\mu| \cdot |\vec{a}| = |(\lambda\mu)\vec{a}|.
>   $$
>
>   Направления также совпадают: вектор поворачивается на $180^\circ$ тогда и только тогда, когда знак меняется нечётное число раз — то есть когда среди $\lambda$ и $\mu$ ровно одно отрицательное число, что равносильно условию $\lambda\mu < 0$.
>
> * **Свойство 6 (дистрибутивность $(\lambda + \mu)\vec{a} = \lambda\vec{a} + \mu\vec{a}$).** При $\vec{a} = \vec{0}$ обе части равны $\vec{0}$; при $\lambda = 0$ или $\mu = 0$ равенство очевидно. Для $\vec{a} \neq \vec{0}$ все векторы лежат на одной прямой, причём достаточно разобрать два случая знаков:
>   1. *$\lambda$ и $\mu$ одного знака* (например, $\lambda, \mu > 0$): оба слагаемых $\lambda\vec{a}$ и $\mu\vec{a}$ сонаправлены с $\vec{a}$, поэтому при их сложении длины складываются: $|\lambda\vec{a} + \mu\vec{a}| = (\lambda + \mu)|\vec{a}| = |(\lambda + \mu)\vec{a}|$, а направление остаётся тем же. Аналогично при $\lambda, \mu < 0$ оба вектора направлены против $\vec{a}$, их длины складываются и дают $|\lambda + \mu| \cdot |\vec{a}|$.
>   2. *$\lambda$ и $\mu$ разных знаков* (пусть $\lambda > 0$ и $\mu < 0$): слагаемые направлены в противоположные стороны, поэтому длина суммы равна модулю разности их длин: $||\lambda\vec{a}| - |\mu\vec{a}|| = |\lambda - |\mu|| \cdot |\vec{a}| = |\lambda + \mu| \cdot |\vec{a}|$, а направление определяется вектором с большей длиной, то есть знаком суммы $\lambda + \mu$.
>
> * **Свойство 7 (дистрибутивность $\lambda(\vec{a} + \vec{b}) = \lambda\vec{a} + \lambda\vec{b}$).** Если $\lambda = 0$ или хотя бы один из векторов нулевой, равенство проверяется сразу. Если $\vec{a}$ и $\vec{b}$ коллинеарны ($\vec{a} \neq \vec{0}$, $\vec{b} = k\vec{a}$), равенство сводится к свойствам 5 и 6:
>
>   $$
>   \lambda(\vec{a} + k\vec{a}) = \lambda((1 + k)\vec{a}) = (\lambda + \lambda k)\vec{a} = \lambda\vec{a} + (\lambda k)\vec{a} = \lambda\vec{a} + \lambda(k\vec{a}).
>   $$
>
>   В основном случае — когда $\vec{a}$ и $\vec{b}$ неколлинеарны и $\lambda \neq 0$ — отложим от общей точки $O$ треугольник сложения: $\overrightarrow{OA} = \vec{a}$, $\overrightarrow{AB} = \vec{b}$, тогда $\overrightarrow{OB} = \vec{a} + \vec{b}$. От той же точки $O$ отложим $\overrightarrow{OA'} = \lambda\vec{a}$, а от $A'$ — вектор $\overrightarrow{A'B'} = \lambda\vec{b}$, так что $\overrightarrow{OB'} = \lambda\vec{a} + \lambda\vec{b}$.
>   Поскольку стороны $OA'$ и $OA$, а также $A'B'$ и $AB$ параллельны (и при одном знаке $\lambda$ углы $\angle OAB$ и $\angle OA'B'$ равны как углы с сонаправленными или противоположно направленными сторонами), а отношения длин одинаковы:
>
>   $$
>   \frac{OA'}{OA} = \frac{A'B'}{AB} = |\lambda|,
>   $$
>
>   треугольники $\triangle OAB$ и $\triangle OA'B'$ подобны по двум сторонам и углу между ними. Следовательно, $\angle AOB = \angle A'OB'$, откуда точки $O, B, B'$ лежат на одной прямой, причём $OB' = |\lambda| \cdot OB$. При $\lambda > 0$ луч $OB'$ совпадает с $OB$, а при $\lambda < 0$ направлен противоположно лучу $OB$ (так как точка $A'$ лежит по другую сторону от $O$). В обоих случаях $\overrightarrow{OB'} = \lambda \overrightarrow{OB}$, то есть $\lambda\vec{a} + \lambda\vec{b} = \lambda(\vec{a} + \vec{b})$. $\blacksquare$

## Орты осей и координаты вектора на плоскости и в пространстве

Геометрические построения удобны для наглядного рассуждения, но выполнять с их помощью точные расчёты на сложных конструкциях неудобно. Чтобы перевести геометрию векторов на язык вычислений над числами, вводят **прямоугольную декартову систему координат**.

На плоскости выбирают точку отсчёта $O$ и две взаимно перпендикулярные оси — ось абсцисс $Ox$ и ось ординат $Oy$ (обозначается система $Oxy$). В трёхмерном пространстве через точку $O$ проводят три попарно перпендикулярные оси: ось абсцисс $Ox$, ось ординат $Oy$ и ось аппликат $Oz$ (система $Oxyz$). Вдоль положительного направления каждой оси откладывают единичные векторы.

> **Орты координатных осей** (или **координатные орты**) — единичные векторы, направленные вдоль положительных направлений осей координат:
> * на плоскости — векторы $\vec{i}$ (вдоль $Ox$) и $\vec{j}$ (вдоль $Oy$);
> * в пространстве — векторы $\vec{i}$ (вдоль $Ox$), $\vec{j}$ (вдоль $Oy$) и $\vec{k}$ (вдоль $Oz$).

Координатные орты имеют длину $1$ ($|\vec{i}| = |\vec{j}| = |\vec{k}| = 1$) и попарно перпендикулярны друг другу.

> [!NOTE] Правая и левая тройки координатных осей
> В пространстве оси обычно ориентируют в виде **правой тройки** (правая система координат): если смотреть из конца третьего орта $\vec{k}$ навстречу его направлению (с положительной полуоси $Oz$ на плоскость $Oxy$), поворот от первого орта $\vec{i}$ к второму орту $\vec{j}$ на угол $90^\circ$ виден происходящим **против часовой стрелки** (правило правой руки). Свойства сложения, умножения на число, длины и коллинеарности одинаково работают и в правой, и в левой системах, но соглашение о правой тройке становится критичным при переходе к векторному произведению в следующих главах.

Любой геометрический вектор удаётся полностью описать при помощи координатных ортов.

> [!IMPORTANT] Теорема (о разложении вектора по ортам осей)
> * **На плоскости:** любой вектор $\vec{a}$ можно **единственным образом** представить в виде:
>
>   $$
>   \vec{a} = a_x\vec{i} + a_y\vec{j}, \quad a_x, a_y \in \mathbb{R}.
>   $$
>
> * **В пространстве:** любой вектор $\vec{a}$ можно **единственным образом** представить в виде:
>
>   $$
>   \vec{a} = a_x\vec{i} + a_y\vec{j} + a_z\vec{k}, \quad a_x, a_y, a_z \in \mathbb{R}.
>   $$

**Доказательство (для пространства; случай плоскости получается отбрасыванием оси $Oz$):**
1. *Существование.* Отложим вектор $\vec{a}$ от начала координат $O$: $\vec{a} = \overrightarrow{OM}$. Опустим из точки $M$ перпендикуляры на координатные оси $Ox$, $Oy$ и $Oz$; пусть их основания — точки $M_x$, $M_y$ и $M_z$ соответственно. (Если $M$ лежит на одной из координатных плоскостей или осей, соответствующие основания просто совпадают с $O$.)
   Векторы $\overrightarrow{OM_x}$, $\overrightarrow{OM_y}$ и $\overrightarrow{OM_z}$ коллинеарны ортам $\vec{i}$, $\vec{j}$ и $\vec{k}$ соответственно. По критерию коллинеарности существуют действительные числа $a_x, a_y, a_z \in \mathbb{R}$ такие, что:

   $$
   \overrightarrow{OM_x} = a_x\vec{i}, \quad \overrightarrow{OM_y} = a_y\vec{j}, \quad \overrightarrow{OM_z} = a_z\vec{k}.
   $$

   Построение задаёт прямоугольный параллелепипед (в вырожденных случаях — прямоугольник или отрезок), в котором $\overrightarrow{OM}$ является главной диагональю. По правилу многоугольника $\overrightarrow{OM} = \overrightarrow{OM_x} + \overrightarrow{OM_y} + \overrightarrow{OM_z}$ (перпендикуляр к плоскости $Oxy$ с основанием $M_{xy}$ даёт $\overrightarrow{OM_x} + \overrightarrow{OM_y} = \overrightarrow{OM_{xy}}$ и далее $\overrightarrow{OM_{xy}} + \overrightarrow{M_{xy}M} = \overrightarrow{OM}$, где $\overrightarrow{M_{xy}M} = \overrightarrow{OM_z}$). Следовательно, $\vec{a} = a_x\vec{i} + a_y\vec{j} + a_z\vec{k}$.

2. *Единственность.* Предположим, нашлись два разложения одного и того же вектора $\vec{a}$:

   $$
   \vec{a} = a_x\vec{i} + a_y\vec{j} + a_z\vec{k} = a'_x\vec{i} + a'_y\vec{j} + a'_z\vec{k}.
   $$

   Перенесём все слагаемые в одну сторону и сгруппируем коэффициенты при одинаковых ортах (используя свойства линейных операций):

   $$
   (a_x - a'_x)\vec{i} + (a_y - a'_y)\vec{j} + (a_z - a'_z)\vec{k} = \vec{0}.
   $$

   Обозначим разности $\Delta_x = a_x - a'_x$, $\Delta_y = a_y - a'_y$, $\Delta_z = a_z - a'_z$. Если бы выполнялось $\Delta_z \neq 0$, равенство можно было бы разделить на $\Delta_z$:

   $$
   \vec{k} = -\frac{\Delta_x}{\Delta_z}\vec{i} - \frac{\Delta_y}{\Delta_z}\vec{j}.
   $$

   В правой части стоит сумма векторов, лежащих в плоскости $Oxy$ (или параллельных ей), поэтому и их сумма лежит в плоскости $Oxy$. Но вектор $\vec{k}$ перпендикулярен плоскости $Oxy$ и не может ей принадлежать. Противоречие доказывает, что $\Delta_z = 0$, то есть $a_z = a'_z$. Точно так же доказывается, что $a_x = a'_x$ и $a_y = a'_y$. $\blacksquare$

> **Координаты вектора $\vec{a}$** в данной системе координат — это единственным образом определённые коэффициенты $a_x, a_y$ (на плоскости) или $a_x, a_y, a_z$ (в пространстве) в разложении вектора $\vec{a}$ по координатным ортам.

Для записи координат вектора используют строку с круглыми скобками и знаком равенства:

$$
\vec{a} = (a_x, a_y) \quad \text{или} \quad \vec{a} = (a_x, a_y, a_z).
$$

В силу единственности разложения **два вектора равны тогда и только тогда, когда равны их соответствующие координаты**:

$$
\vec{a} = \vec{b} \iff a_x = b_x, \; a_y = b_y, \; a_z = b_z.
$$

В частности, в трёхмерном пространстве $\vec{0} = (0, 0, 0)$, а сами координатные орты имеют координаты $\vec{i} = (1, 0, 0)$, $\vec{j} = (0, 1, 0)$, $\vec{k} = (0, 0, 1)$.

<svg viewBox="0 0 540 205" style="max-width: 580px; width: 100%; height: auto; display: block; margin: 1em auto;">
  <defs>
    <marker id="v5-curr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="currentColor"/>
    </marker>
    <marker id="v5-blue" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#3b82f6"/>
    </marker>
    <marker id="v5-amber" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#f59e0b"/>
    </marker>
  </defs>
  <line x1="45" y1="165" x2="225" y2="165" stroke="currentColor" stroke-opacity="0.7" stroke-width="1.3" marker-end="url(#v5-curr)"/>
  <line x1="45" y1="165" x2="45" y2="20" stroke="currentColor" stroke-opacity="0.7" stroke-width="1.3" marker-end="url(#v5-curr)"/>
  <text x="220" y="182" fill="currentColor" font-size="13" font-style="italic" font-family="sans-serif">x</text>
  <text x="29" y="28" fill="currentColor" font-size="13" font-style="italic" font-family="sans-serif">y</text>
  <text x="30" y="179" fill="currentColor" font-size="13" font-family="sans-serif">O</text>
  <line x1="185" y1="55" x2="185" y2="165" stroke="currentColor" stroke-opacity="0.38" stroke-dasharray="4 4" stroke-width="1.2"/>
  <line x1="185" y1="55" x2="45" y2="55" stroke="currentColor" stroke-opacity="0.38" stroke-dasharray="4 4" stroke-width="1.2"/>
  <line x1="45" y1="165" x2="82" y2="165" stroke="#f59e0b" stroke-width="2.4" marker-end="url(#v5-amber)"/>
  <line x1="45" y1="165" x2="45" y2="128" stroke="#f59e0b" stroke-width="2.4" marker-end="url(#v5-amber)"/>
  <text x="64" y="180" fill="#f59e0b" font-size="13" font-weight="bold" font-style="italic" font-family="sans-serif">i</text>
  <text x="29" y="148" fill="#f59e0b" font-size="13" font-weight="bold" font-style="italic" font-family="sans-serif">j</text>
  <line x1="45" y1="165" x2="185" y2="55" stroke="#3b82f6" stroke-width="2.6" marker-end="url(#v5-blue)"/>
  <text x="115" y="98" fill="#3b82f6" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">a</text>
  <text x="178" y="182" fill="currentColor" font-size="12" font-style="italic" font-family="sans-serif">aₓ</text>
  <text x="24" y="60" fill="currentColor" font-size="12" font-style="italic" font-family="sans-serif">aᵧ</text>
  <line x1="252" y1="15" x2="252" y2="190" stroke="currentColor" stroke-opacity="0.2" stroke-width="1.2"/>
  <line x1="355" y1="130" x2="275" y2="188" stroke="currentColor" stroke-opacity="0.7" stroke-width="1.3" marker-end="url(#v5-curr)"/>
  <line x1="355" y1="130" x2="515" y2="130" stroke="currentColor" stroke-opacity="0.7" stroke-width="1.3" marker-end="url(#v5-curr)"/>
  <line x1="355" y1="130" x2="355" y2="18" stroke="currentColor" stroke-opacity="0.7" stroke-width="1.3" marker-end="url(#v5-curr)"/>
  <text x="266" y="196" fill="currentColor" font-size="13" font-style="italic" font-family="sans-serif">x</text>
  <text x="512" y="146" fill="currentColor" font-size="13" font-style="italic" font-family="sans-serif">y</text>
  <text x="363" y="25" fill="currentColor" font-size="13" font-style="italic" font-family="sans-serif">z</text>
  <text x="340" y="124" fill="currentColor" font-size="13" font-family="sans-serif">O</text>
  <line x1="313" y1="161" x2="423" y2="161" stroke="currentColor" stroke-opacity="0.35" stroke-dasharray="4 4" stroke-width="1.2"/>
  <line x1="465" y1="130" x2="423" y2="161" stroke="currentColor" stroke-opacity="0.35" stroke-dasharray="4 4" stroke-width="1.2"/>
  <line x1="313" y1="161" x2="313" y2="79" stroke="currentColor" stroke-opacity="0.35" stroke-dasharray="4 4" stroke-width="1.2"/>
  <line x1="355" y1="48" x2="313" y2="79" stroke="currentColor" stroke-opacity="0.35" stroke-dasharray="4 4" stroke-width="1.2"/>
  <line x1="465" y1="130" x2="465" y2="48" stroke="currentColor" stroke-opacity="0.35" stroke-dasharray="4 4" stroke-width="1.2"/>
  <line x1="355" y1="48" x2="465" y2="48" stroke="currentColor" stroke-opacity="0.35" stroke-dasharray="4 4" stroke-width="1.2"/>
  <line x1="423" y1="161" x2="423" y2="79" stroke="currentColor" stroke-opacity="0.35" stroke-dasharray="4 4" stroke-width="1.2"/>
  <line x1="313" y1="79" x2="423" y2="79" stroke="currentColor" stroke-opacity="0.35" stroke-dasharray="4 4" stroke-width="1.2"/>
  <line x1="465" y1="48" x2="423" y2="79" stroke="currentColor" stroke-opacity="0.35" stroke-dasharray="4 4" stroke-width="1.2"/>
  <line x1="355" y1="130" x2="332" y2="147" stroke="#f59e0b" stroke-width="2.2" marker-end="url(#v5-amber)"/>
  <line x1="355" y1="130" x2="392" y2="130" stroke="#f59e0b" stroke-width="2.2" marker-end="url(#v5-amber)"/>
  <line x1="355" y1="130" x2="355" y2="95" stroke="#f59e0b" stroke-width="2.2" marker-end="url(#v5-amber)"/>
  <text x="331" y="138" fill="#f59e0b" font-size="12" font-weight="bold" font-style="italic" font-family="sans-serif">i</text>
  <text x="378" y="144" fill="#f59e0b" font-size="12" font-weight="bold" font-style="italic" font-family="sans-serif">j</text>
  <text x="361" y="106" fill="#f59e0b" font-size="12" font-weight="bold" font-style="italic" font-family="sans-serif">k</text>
  <line x1="355" y1="130" x2="423" y2="79" stroke="#3b82f6" stroke-width="2.6" marker-end="url(#v5-blue)"/>
  <text x="396" y="114" fill="#3b82f6" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">a</text>
  <text x="295" y="160" fill="currentColor" font-size="12" font-style="italic" font-family="sans-serif">aₓ</text>
  <text x="462" y="145" fill="currentColor" font-size="12" font-style="italic" font-family="sans-serif">aᵧ</text>
  <text x="334" y="52" fill="currentColor" font-size="12" font-style="italic" font-family="sans-serif">a_z</text>
</svg>

*Разложение вектора $\vec{a}$ по ортам на плоскости ($\vec{a} = a_x\vec{i} + a_y\vec{j}$) и в пространстве ($\vec{a} = a_x\vec{i} + a_y\vec{j} + a_z\vec{k}$).*

> [!NOTE] Круглые и фигурные скобки, точка и вектор
> В отечественной учебной литературе координаты вектора часто записывают в **фигурных** скобках — например, $\vec{a} = \{a_x, a_y, a_z\}$ — чтобы визуально отличать вектор от точки $M(x, y, z)$, для которой используют круглые скобки и не ставят знак равенства. В линейной алгебре и многомерной геометрии для векторов стандартно используют **круглые** скобки $\vec{a} = (a_x, a_y, a_z)$ (с тем же знаком равенства, которого нет в записи точки $M(x, y, z)$). Чтобы сохранить единую запись при переходе к $n$-мерному пространству, далее используются круглые скобки.

---

## Сложение векторов и умножение вектора на число в координатах

Разложение по ортам вместе с восемью свойствами линейных операций мгновенно переводит геометрические действия над векторами в обычные операции над числами.

Пусть в пространстве заданы два вектора своими координатами:

$$
\vec{a} = (a_x, a_y, a_z) = a_x\vec{i} + a_y\vec{j} + a_z\vec{k}, \qquad \vec{b} = (b_x, b_y, b_z) = b_x\vec{i} + b_y\vec{j} + b_z\vec{k}.
$$

Используя коммутативность, ассоциативность и дистрибутивность, раскроем скобки при сложении:

$$
\vec{a} + \vec{b} = (a_x\vec{i} + a_y\vec{j} + a_z\vec{k}) + (b_x\vec{i} + b_y\vec{j} + b_z\vec{k}) = (a_x + b_x)\vec{i} + (a_y + b_y)\vec{j} + (a_z + b_z)\vec{k}.
$$

Аналогично при умножении $\vec{a}$ на число $\lambda \in \mathbb{R}$:

$$
\lambda\vec{a} = \lambda(a_x\vec{i} + a_y\vec{j} + a_z\vec{k}) = (\lambda a_x)\vec{i} + (\lambda a_y)\vec{j} + (\lambda a_z)\vec{k}.
$$

Поскольку координаты в разложении по ортам единственны, получаем простые правила:

1. **При сложении (вычитании) векторов их одноимённые координаты складываются (вычитаются):**

   $$
   \vec{a} \pm \vec{b} = (a_x \pm b_x, \; a_y \pm b_y, \; a_z \pm b_z).
   $$

2. **При умножении вектора на число каждая его координата умножается на это число:**

   $$
   \lambda\vec{a} = (\lambda a_x, \; \lambda a_y, \; \lambda a_z).
   $$

На плоскости действуют точно такие же правила (с двумя координатами $x$ и $y$ вместо трёх).

**Пример:** Для векторов $\vec{a} = (3, -1, 2)$ и $\vec{b} = (1, 4, -5)$:

$$
2\vec{a} - 3\vec{b} = (2 \cdot 3, \, 2 \cdot (-1), \, 2 \cdot 2) - (3 \cdot 1, \, 3 \cdot 4, \, 3 \cdot (-5)) = (6 - 3, \, -2 - 12, \, 4 - (-15)) = (3, -14, 19).
$$

---

## Длина вектора и направляющие косинусы

Координаты позволяют точно вычислить как длину вектора, так и углы, под которыми он наклонён к осям координат.

### Длина вектора, заданного координатами

> [!IMPORTANT] Теорема (о длине вектора в координатах)
> * **На плоскости** длина вектора $\vec{a} = (a_x, a_y)$ равна:
>
>   $$
>   |\vec{a}| = \sqrt{a_x^2 + a_y^2}.
>   $$
>
> * **В пространстве** длина вектора $\vec{a} = (a_x, a_y, a_z)$ равна:
>
>   $$
>   |\vec{a}| = \sqrt{a_x^2 + a_y^2 + a_z^2}.
>   $$

**Доказательство:**
На плоскости, если $a_x \neq 0$ и $a_y \neq 0$, вектор $\vec{a} = \overrightarrow{OM}$ служит гипотенузой прямоугольного треугольника с катетами длиной $|a_x|$ и $|a_y|$. По теореме Пифагора $|\vec{a}|^2 = |a_x|^2 + |a_y|^2 = a_x^2 + a_y^2$. Если одна или обе координаты равны нулю (например, $a_y = 0$), формула остаётся верной: $|\vec{a}| = |a_x| = \sqrt{a_x^2 + 0^2}$.

В пространстве (см. предыдущий рисунок) при ненулевых координатах длина проекции в плоскости $Oxy$ равна $OM_{xy} = \sqrt{a_x^2 + a_y^2}$ (как гипотенуза прямоугольного треугольника с катетами $|a_x|$ и $|a_y|$). Поскольку ребро $M_{xy}M$ перпендикулярно плоскости $Oxy$, треугольник $\triangle OM_{xy}M$ тоже прямоугольный, с катетами $OM_{xy}$ и $|a_z|$. Применяя теорему Пифагора второй раз, получаем:

$$
|\vec{a}|^2 = OM^2 = OM_{xy}^2 + |a_z|^2 = a_x^2 + a_y^2 + a_z^2.
$$

Извлечение арифметического квадратного корня (так как $|\vec{a}| \ge 0$) даёт искомую формулу. Если часть координат равна нулю, пространство сводится к плоскости или координатной оси, и формула также сохраняется. $\blacksquare$

### Направляющие косинусы вектора

Чтобы задать направление ненулевого вектора $\vec{a} \neq \vec{0}$ в пространстве с помощью углов, рассматривают углы $\alpha, \beta, \gamma$, которые этот вектор (отложенный от начала координат $O$) образует с положительными направлениями осей $Ox$, $Oy$, $Oz$ — то есть с ортами $\vec{i}, \vec{j}, \vec{k}$. По определению угла между векторами каждый из этих углов лежит в пределах от $0$ до $\pi$ ($0^\circ \le \alpha, \beta, \gamma \le 180^\circ$).

> **Направляющие косинусы** ненулевого вектора $\vec{a}$ — это косинусы углов $\alpha, \beta, \gamma$ между вектором $\vec{a}$ и положительными направлениями координатных осей $Ox, Oy, Oz$ (на плоскости — $\cos\alpha$ и $\cos\beta$).

Установим связь направляющих косинусов с координатами вектора $\vec{a} = (a_x, a_y, a_z)$:

* Если $a_x > 0$, угол $\alpha$ острый ($0 < \alpha < \frac{\pi}{2}$), и в прямоугольном треугольнике $\triangle OM_xM$ (где $\angle OM_xM = 90^\circ$) прилежащий катет $OM_x = a_x$, а гипотенуза $OM = |\vec{a}|$, откуда $\cos\alpha = \frac{a_x}{|\vec{a}|}$.
* Если $a_x < 0$, угол $\alpha$ тупой ($\frac{\pi}{2} < \alpha < \pi$), точка $M_x$ лежит на отрицательной полуоси $Ox$ на расстоянии $|a_x| = -a_x$ от $O$, и смежный острый угол равен $\pi - \alpha$. Тогда $\cos(\pi - \alpha) = \frac{|a_x|}{|\vec{a}|} = \frac{-a_x}{|\vec{a}|}$, а поскольку $\cos\alpha = -\cos(\pi - \alpha)$, знак «минус» уходит: $\cos\alpha = \frac{a_x}{|\vec{a}|}$.
* В граничных случаях: при $a_x = 0$ вектор перпендикулярен $Ox$ ($\alpha = \frac{\pi}{2}$, $\cos\alpha = 0$); если вектор лежит на оси $Ox$, то $\alpha = 0$ ($\cos\alpha = 1$ при $a_x > 0$) или $\alpha = \pi$ ($\cos\alpha = -1$ при $a_x < 0$).

Проведя то же рассуждение для осей $Oy$ и $Oz$, получаем общие формулы направляющих косинусов для $\vec{a} \neq \vec{0}$:

$$
\cos\alpha = \frac{a_x}{|\vec{a}|}, \qquad \cos\beta = \frac{a_y}{|\vec{a}|}, \qquad \cos\gamma = \frac{a_z}{|\vec{a}|}.
$$

*(На плоскости используются первые две формулы: $\cos\alpha = \frac{a_x}{|\vec{a}|}$ и $\cos\beta = \frac{a_y}{|\vec{a}|}$.)*

<svg viewBox="0 0 490 185" style="max-width: 530px; width: 100%; height: auto; display: block; margin: 1em auto;">
  <defs>
    <marker id="v6-curr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="currentColor"/>
    </marker>
    <marker id="v6-blue" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#3b82f6"/>
    </marker>
  </defs>
  <line x1="45" y1="150" x2="215" y2="150" stroke="currentColor" stroke-opacity="0.7" stroke-width="1.3" marker-end="url(#v6-curr)"/>
  <line x1="45" y1="150" x2="45" y2="20" stroke="currentColor" stroke-opacity="0.7" stroke-width="1.3" marker-end="url(#v6-curr)"/>
  <text x="210" y="167" fill="currentColor" font-size="13" font-style="italic" font-family="sans-serif">x</text>
  <text x="30" y="28" fill="currentColor" font-size="13" font-style="italic" font-family="sans-serif">y</text>
  <text x="31" y="163" fill="currentColor" font-size="13" font-family="sans-serif">O</text>
  <line x1="175" y1="55" x2="175" y2="150" stroke="currentColor" stroke-opacity="0.35" stroke-dasharray="4 4" stroke-width="1.2"/>
  <line x1="175" y1="55" x2="45" y2="55" stroke="currentColor" stroke-opacity="0.35" stroke-dasharray="4 4" stroke-width="1.2"/>
  <path d="M 88 150 A 43 43 0 0 0 79.7 124.6" fill="none" stroke="#ef4444" stroke-width="1.8"/>
  <text x="93" y="138" fill="#ef4444" font-size="13" font-style="italic" font-family="sans-serif">α</text>
  <path d="M 45 102 A 48 48 0 0 1 83.8 121.7" fill="none" stroke="#10b981" stroke-width="1.8"/>
  <text x="58" y="99" fill="#10b981" font-size="13" font-style="italic" font-family="sans-serif">β</text>
  <line x1="45" y1="150" x2="175" y2="55" stroke="#3b82f6" stroke-width="2.6" marker-end="url(#v6-blue)"/>
  <text x="125" y="82" fill="#3b82f6" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">a</text>
  <text x="168" y="166" fill="currentColor" font-size="12" font-style="italic" font-family="sans-serif">aₓ</text>
  <text x="24" y="60" fill="currentColor" font-size="12" font-style="italic" font-family="sans-serif">aᵧ</text>
  <line x1="240" y1="15" x2="240" y2="170" stroke="currentColor" stroke-opacity="0.2" stroke-width="1.2"/>
  <line x1="330" y1="125" x2="262" y2="173" stroke="currentColor" stroke-opacity="0.7" stroke-width="1.3" marker-end="url(#v6-curr)"/>
  <line x1="330" y1="125" x2="475" y2="125" stroke="currentColor" stroke-opacity="0.7" stroke-width="1.3" marker-end="url(#v6-curr)"/>
  <line x1="330" y1="125" x2="330" y2="18" stroke="currentColor" stroke-opacity="0.7" stroke-width="1.3" marker-end="url(#v6-curr)"/>
  <text x="253" y="180" fill="currentColor" font-size="13" font-style="italic" font-family="sans-serif">x</text>
  <text x="470" y="141" fill="currentColor" font-size="13" font-style="italic" font-family="sans-serif">y</text>
  <text x="338" y="25" fill="currentColor" font-size="13" font-style="italic" font-family="sans-serif">z</text>
  <text x="315" y="121" fill="currentColor" font-size="13" font-family="sans-serif">O</text>
  <line x1="425" y1="62" x2="298" y2="148" stroke="currentColor" stroke-opacity="0.3" stroke-dasharray="3 3" stroke-width="1.1"/>
  <line x1="425" y1="62" x2="425" y2="125" stroke="currentColor" stroke-opacity="0.3" stroke-dasharray="3 3" stroke-width="1.1"/>
  <line x1="425" y1="62" x2="330" y2="62" stroke="currentColor" stroke-opacity="0.3" stroke-dasharray="3 3" stroke-width="1.1"/>
  <path d="M 303 144 A 34 34 0 0 0 356 108" fill="none" stroke="#ef4444" stroke-width="1.7"/>
  <text x="342" y="148" fill="#ef4444" font-size="12" font-style="italic" font-family="sans-serif">α</text>
  <path d="M 378 125 A 48 48 0 0 0 370 98" fill="none" stroke="#10b981" stroke-width="1.7"/>
  <text x="383" y="114" fill="#10b981" font-size="12" font-style="italic" font-family="sans-serif">β</text>
  <path d="M 330 85 A 40 40 0 0 1 363 103" fill="none" stroke="#f59e0b" stroke-width="1.7"/>
  <text x="342" y="83" fill="#f59e0b" font-size="12" font-style="italic" font-family="sans-serif">γ</text>
  <line x1="330" y1="125" x2="425" y2="62" stroke="#3b82f6" stroke-width="2.6" marker-end="url(#v6-blue)"/>
  <text x="394" y="74" fill="#3b82f6" font-size="14" font-weight="bold" font-style="italic" font-family="sans-serif">a</text>
</svg>

*Углы $\alpha, \beta$ (на плоскости) и $\alpha, \beta, \gamma$ (в пространстве) между вектором $\vec{a}$ и положительными направлениями осей.*

Из формул направляющих косинусов сразу вытекают два важных свойства:

1. **Основное тождество для направляющих косинусов:** сумма квадратов всех направляющих косинусов ненулевого вектора всегда равна единице:

   $$
   \cos^2\alpha + \cos^2\beta + \cos^2\gamma = \frac{a_x^2 + a_y^2 + a_z^2}{|\vec{a}|^2} = \frac{|\vec{a}|^2}{|\vec{a}|^2} = 1.
   $$

   *(На плоскости аналогично: $\cos^2\alpha + \cos^2\beta = 1$.)* Это означает, что углы $\alpha, \beta, \gamma$ нельзя задать тремя произвольными числами: два угла с точностью до знака третьего косинуса определяют третий угол.
2. **Координаты орта:** подставив координаты $\vec{a}$ в формулу нормировки $\vec{a}^{\,0} = \frac{1}{|\vec{a}|}\vec{a}$, получаем:

   $$
   \vec{a}^{\,0} = \left(\frac{a_x}{|\vec{a}|}, \; \frac{a_y}{|\vec{a}|}, \; \frac{a_z}{|\vec{a}|}\right) = (\cos\alpha, \; \cos\beta, \; \cos\gamma).
   $$

   **Координаты орта любого ненулевого вектора — это его направляющие косинусы.**

**Пример:** Для вектора $\vec{a} = (2, -1, 2)$ вычислим длину, направляющие косинусы и орт:
* Длина: $|\vec{a}| = \sqrt{2^2 + (-1)^2 + 2^2} = \sqrt{4 + 1 + 4} = \sqrt{9} = 3$.
* Направляющие косинусы: $\cos\alpha = \frac{2}{3}$, $\cos\beta = -\frac{1}{3}$, $\cos\gamma = \frac{2}{3}$. Проверка: $\left(\frac{2}{3}\right)^2 + \left(-\frac{1}{3}\right)^2 + \left(\frac{2}{3}\right)^2 = \frac{4 + 1 + 4}{9} = 1$.
* Орт вектора: $\vec{a}^{\,0} = \left(\frac{2}{3}, -\frac{1}{3}, \frac{2}{3}\right)$.

*(Для нулевого вектора $\vec{0}$ длина $|\vec{0}| = 0$, поэтому направляющие косинусы, как и орт, не определены.)*

---

## Условие коллинеарности векторов, заданных координатами

В первой части был доказан критерий: при $\vec{a} \neq \vec{0}$ вектор $\vec{b}$ коллинеарен $\vec{a}$ тогда и только тогда, когда $\vec{b} = \lambda\vec{a}$ для некоторого $\lambda \in \mathbb{R}$. В координатах это равенство распадается на равенство каждой координаты по отдельности.

> [!IMPORTANT] Теорема (условие коллинеарности в координатах)
> Векторы $\vec{a} = (a_x, a_y, a_z) \neq \vec{0}$ и $\vec{b} = (b_x, b_y, b_z)$ коллинеарны **тогда и только тогда**, когда их координаты пропорциональны, то есть существует число $\lambda \in \mathbb{R}$ такое, что:
>
> $$
> b_x = \lambda a_x, \qquad b_y = \lambda a_y, \qquad b_z = \lambda a_z.
> $$

Если **все** координаты вектора $\vec{a}$ отличны от нуля ($a_x \neq 0, \, a_y \neq 0, \, a_z \neq 0$), число $\lambda$ можно выразить из каждого равенства и записать условие в виде пропорции:

$$
\frac{b_x}{a_x} = \frac{b_y}{a_y} = \frac{b_z}{a_z} \quad (=\lambda).
$$

На плоскости это соответственно $\frac{b_x}{a_x} = \frac{b_y}{a_y}$ (при $a_x, a_y \neq 0$). По знаку общего отношения $\lambda$ сразу видно взаимное направление ненулевых коллинеарных векторов: при $\lambda > 0$ они сонаправлены, при $\lambda < 0$ — противоположно направлены.

> [!NOTE] Ловушка с нулевыми координатами при проверке коллинеарности
> Записывать условие коллинеарности через дроби $\frac{b_x}{a_x} = \frac{b_y}{a_y} = \frac{b_z}{a_z}$ буквально можно **только тогда, когда ни одна координата вектора $\vec{a}$ не равна нулю**. На практике часто используют *условную* запись с нулём в знаменателе, договариваясь считать, что если знаменатель равен $0$, то и соответствующий числитель обязан равняться $0$ (ведь $b_i = \lambda \cdot 0 = 0$).
>
> Однако в выкладках надёжнее либо проверять существование общего множителя $\lambda$ напрямую из системы $b_i = \lambda a_i$, либо пользоваться записью без деления:
> * на плоскости: $a_x b_y - a_y b_x = 0$;
> * в пространстве: равенства нулю всех трёх попарных разностей $a_x b_y - a_y b_x = 0$, $a_y b_z - a_z b_y = 0$, $a_x b_z - a_z b_x = 0$ (они равносильны пропорциональности координат без всяких ограничений на нули).

**Примеры:**
1. Векторы $\vec{a} = (2, -4, 6)$ и $\vec{b} = (-3, 6, -9)$ коллинеарны и противоположно направлены: $\frac{-3}{2} = \frac{6}{-4} = \frac{-9}{6} = -\frac{3}{2}$, то есть $\vec{b} = -\frac{3}{2}\vec{a}$.
2. Векторы $\vec{p} = (2, 0, -4)$ и $\vec{q} = (-3, 0, 6)$ коллинеарны, так как $\vec{q} = -\frac{3}{2}\vec{p}$ (вторая координата у обоих равна $0$). А вот вектор $\vec{r} = (-3, 1, 6)$ не коллинеарен $\vec{p}$: для первой и третьей координат множитель равен $-\frac{3}{2}$, но $1 \neq -\frac{3}{2} \cdot 0$.

---

## Нахождение координат вектора по координатам его конца и начала

Во многих задачах вектор задан не своими координатами напрямую, а двумя точками — своим началом $A(x_A, y_A, z_A)$ и концом $B(x_B, y_B, z_B)$. Чтобы найти координаты вектора $\overrightarrow{AB}$, связывают точки с началом координат $O(0, 0, 0)$.

> **Радиус-вектором точки $M$** называют вектор $\overrightarrow{OM}$, идущий из начала координат $O$ в точку $M$.

По построению из теоремы о разложении по ортам координаты радиус-вектора $\overrightarrow{OM}$ совпадают с координатами самой точки $M$:

$$
M(x_M, y_M, z_M) \iff \overrightarrow{OM} = (x_M, y_M, z_M).
$$

Теперь рассмотрим треугольник, образованный точками $O$, $A$ и $B$. По правилу треугольника для сложения векторов:

$$
\overrightarrow{OA} + \overrightarrow{AB} = \overrightarrow{OB},
$$

откуда:

$$
\overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA}.
$$

Подставив координаты радиус-векторов $\overrightarrow{OB} = (x_B, y_B, z_B)$ и $\overrightarrow{OA} = (x_A, y_A, z_A)$ и выполнив вычитание по координатам, получаем основное правило.

> [!IMPORTANT] Теорема (координаты вектора через координаты начала и конца)
> Если точка $A$ имеет координаты $(x_A, y_A, z_A)$, а точка $B$ — координаты $(x_B, y_B, z_B)$, то координаты вектора $\overrightarrow{AB}$ равны разности соответствующих координат **конца** и **начала**:
>
> $$
> \overrightarrow{AB} = (x_B - x_A, \; y_B - y_A, \; z_B - z_A).
> $$
>
> *(На плоскости: $\overrightarrow{AB} = (x_B - x_A, \; y_B - y_A)$.)*

<svg viewBox="0 0 430 175" style="max-width: 470px; width: 100%; height: auto; display: block; margin: 1em auto;">
  <defs>
    <marker id="v7-curr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="currentColor"/>
    </marker>
    <marker id="v7-blue" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#3b82f6"/>
    </marker>
    <marker id="v7-green" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#10b981"/>
    </marker>
    <marker id="v7-red" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#ef4444"/>
    </marker>
  </defs>
  <line x1="45" y1="145" x2="395" y2="145" stroke="currentColor" stroke-opacity="0.7" stroke-width="1.3" marker-end="url(#v7-curr)"/>
  <line x1="45" y1="145" x2="45" y2="15" stroke="currentColor" stroke-opacity="0.7" stroke-width="1.3" marker-end="url(#v7-curr)"/>
  <text x="390" y="162" fill="currentColor" font-size="13" font-style="italic" font-family="sans-serif">x</text>
  <text x="30" y="23" fill="currentColor" font-size="13" font-style="italic" font-family="sans-serif">y</text>
  <text x="31" y="159" fill="currentColor" font-size="13" font-family="sans-serif">O</text>
  <line x1="150" y1="100" x2="150" y2="145" stroke="currentColor" stroke-opacity="0.32" stroke-dasharray="4 4" stroke-width="1.1"/>
  <line x1="150" y1="100" x2="45" y2="100" stroke="currentColor" stroke-opacity="0.32" stroke-dasharray="4 4" stroke-width="1.1"/>
  <line x1="320" y1="42" x2="320" y2="145" stroke="currentColor" stroke-opacity="0.32" stroke-dasharray="4 4" stroke-width="1.1"/>
  <line x1="320" y1="42" x2="45" y2="42" stroke="currentColor" stroke-opacity="0.32" stroke-dasharray="4 4" stroke-width="1.1"/>
  <text x="143" y="161" fill="currentColor" font-size="11" font-style="italic" font-family="sans-serif">x_A</text>
  <text x="313" y="161" fill="currentColor" font-size="11" font-style="italic" font-family="sans-serif">x_B</text>
  <text x="23" y="104" fill="currentColor" font-size="11" font-style="italic" font-family="sans-serif">y_A</text>
  <text x="23" y="46" fill="currentColor" font-size="11" font-style="italic" font-family="sans-serif">y_B</text>
  <line x1="45" y1="145" x2="150" y2="100" stroke="#3b82f6" stroke-width="2.3" marker-end="url(#v7-blue)"/>
  <line x1="45" y1="145" x2="320" y2="42" stroke="#10b981" stroke-width="2.3" marker-end="url(#v7-green)"/>
  <line x1="150" y1="100" x2="320" y2="42" stroke="#ef4444" stroke-width="2.6" marker-end="url(#v7-red)"/>
  <circle cx="150" cy="100" r="3" fill="currentColor"/>
  <circle cx="320" cy="42" r="3" fill="currentColor"/>
  <text x="154" y="114" fill="currentColor" font-size="13" font-weight="bold" font-family="sans-serif">A</text>
  <text x="325" y="39" fill="currentColor" font-size="13" font-weight="bold" font-family="sans-serif">B</text>
  <text x="90" y="115" fill="#3b82f6" font-size="12" font-weight="bold" font-style="italic" font-family="sans-serif">OA</text>
  <text x="180" y="74" fill="#10b981" font-size="12" font-weight="bold" font-style="italic" font-family="sans-serif">OB</text>
  <text x="242" y="88" fill="#ef4444" font-size="13" font-weight="bold" font-style="italic" font-family="sans-serif">AB</text>
</svg>

*Нахождение координат вектора $\overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA}$ через радиус-векторы его конца и начала.*

Немедленным следствием этой теоремы и формулы длины вектора становится **расстояние между двумя точками** $A$ и $B$:

$$
AB = |\overrightarrow{AB}| = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2}.
$$

**Пример:** Найдём координаты вектора $\overrightarrow{AB}$ и длину отрезка $AB$ для точек $A(2, -3, 5)$ и $B(-1, 1, 5)$:

$$
\overrightarrow{AB} = (-1 - 2, \; 1 - (-3), \; 5 - 5) = (-3, 4, 0),
$$

$$
AB = |\overrightarrow{AB}| = \sqrt{(-3)^2 + 4^2 + 0^2} = \sqrt{9 + 16 + 0} = 5.
$$

Обратный вектор $\overrightarrow{BA} = -\overrightarrow{AB} = (3, -4, 0)$ имеет противоположные знаки координат и ту же длину $5$.