---
tags: [portfolio, components, shadcn, radix, primitives]
---

# UI Primitives

> [[../INDEX|← Back to Index]] · [[00-overview|Component Map]]

## CometCard — `src/components/ui/comet-card.tsx` (Community 13, 17 edges)

See [[../architecture/04-design-system|Design System]] for full contract. The cross-community card primitive used in CertificationsSection, ContactPanel, ExperienceCard, and more.

## Sidebar — `src/components/ui/sidebar.tsx` (Communities 6, 9, 67)

The most complex primitive. Community 67 owns the hook:

```typescript
// Community 67
function useSidebar(): SidebarContext   // 20 edges — god node
function Sidebar(): JSX.Element
function SidebarToggle(): JSX.Element
```

Community 6 owns the sub-components:
```typescript
function SidebarProvider(props): JSX.Element
function SidebarFooter(): JSX.Element
function SidebarGroup(): JSX.Element
function SidebarGroupAction(): JSX.Element
function SidebarGroupContent(): JSX.Element
function SidebarGroupLabel(): JSX.Element
// + more sidebar sub-components
```

Community 9 owns navigation use: `Sheet()`, `SheetContent()` used for mobile sidebar.

## Card — `src/components/ui/card.tsx` (Community 47)

```typescript
function Card(): JSX.Element
function CardHeader(): JSX.Element
function CardTitle(): JSX.Element
function CardContent(): JSX.Element
function CardFooter(): JSX.Element
function CardDescription(): JSX.Element
function CardAction(): JSX.Element  // shadcn v2 addition
```

All call `cn()`. Standard shadcn Card implementation.

## Dropdown Menu — `src/components/ui/dropdown-menu.tsx` (Community 24)

```typescript
function DropdownMenuCheckboxItem()
function DropdownMenuContent()
function DropdownMenuItem()
function DropdownMenuLabel()
function DropdownMenuRadioItem()
function DropdownMenuSeparator()
function DropdownMenuShortcut()
function DropdownMenuSubContent()
function DropdownMenuTrigger()  // implied
```

## Sheet — `src/components/ui/sheet.tsx` (Community 9)

Used for mobile sidebar overlay. `Sheet()`, `SheetContent()` from Radix.

## Chart — `src/components/ui/chart.tsx` (Community 28)

Recharts-based chart primitives:
```typescript
type ChartConfig = Record<string, { label: string; color?: string }>
interface ChartContextProps { config: ChartConfig }
const ChartContext: React.Context<ChartContextProps>
function ChartContainer(props: { config: ChartConfig }): JSX.Element
function ChartTooltipContent(props: ChartTooltipContentProps): JSX.Element
function ChartLegendContent(props: ChartLegendContentProps): JSX.Element
type ChartPayloadItem = { name: string; value: number; ... }
```

## Input — `src/components/ui/` (Community 6)

`Input()` is in Community 6 alongside `cn()` and sidebar primitives.

## Tooltip — `src/components/ui/tooltip.tsx` (Community 6)

Standard Radix tooltip primitive.

## Layout Text Flip — `src/components/ui/layout-text-flip.tsx`

Animated text flip/swap component for hero headline transitions.

## Spinner — `src/components/ui/spinner.tsx`

Simple loading spinner. **Calls `cn()`** — noted as a surprising connection in the graph.

## Hooks

| Hook | File | Community | Purpose |
|------|------|-----------|---------|
| `useIridescentEffect()` | `src/hooks/useIridescentEffect.ts` | 3 | Mouse-driven iridescent glow (15 edges) |
| `useIsMobile()` | `src/hooks/use-mobile.ts` | 22 | Viewport width < 768px check |
| `useActiveSection()` | `src/hooks/useActiveSection.ts` | — | IntersectionObserver for active nav section |
| `useShowOnScroll()` | `src/hooks/useShowOnScroll.ts` | — | Scroll visibility trigger |

### useIridescentEffect (15 edges — god node)

```typescript
interface UseIridescentEffectOptions {
  intensity?: number
  colors?: string[]
}
function useIridescentEffect(ref: RefObject<HTMLElement>, opts?: UseIridescentEffectOptions): void
```

Used on: profile name in Hero, social buttons in Contact, nav links.

## See Also
- [[../architecture/04-design-system|Design System (cn, cosmic-card, float-btn)]]
