from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

def all_legendary_birds_in_play_condition(calc, carrier):
    if calc.attacker is None or carrier.owning_player_id != calc.attacker.owning_player_id:
        return False
    is_zapdos_in_play_condition = is_bird_in_play(calc, carrier, "Zapdos")
    is_articuno_in_play_condition = is_bird_in_play(calc, carrier, "Articuno")
    is_moltres_in_play_condition = is_bird_in_play(calc, carrier, "Moltres")

    return is_articuno_in_play_condition and is_zapdos_in_play_condition and is_moltres_in_play_condition

def is_bird_in_play(calc, carrier, bird_name):
    return any(
        p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == bird_name
        for p in calc.board.pokemon_in_play(carrier.owning_player_id)
    )

async def frosty_flapping(ctx):
    """Attach a Basic Water Energy card from your hand to this Pokemon."""
    energies = [c for c in ctx.hand() if is_water_energy_card(c)]
    if not energies:
        return
    if not await ctx.ask_yes_no(
            "Attach a Water Energy card from your hand to this Pokémon?"
    ):
        return
    picked = await ctx.choose_cards(
        energies, 1, minimum=1, prompt="Choose a Water Energy card to attach"
    )
    if picked:
        await ctx.attach_energy(picked[0], ctx.attacker)

async def hail(ctx):
    """30 to each of your opponent's pokemon"""
    targets = ctx.opponent_pokemon_in_play()
    for pokemon in targets:
        await ctx.deal_damage(
            30, target=pokemon, apply_modifiers=(pokemon is ctx.opponent_active())
        )


card = PokemonCardDef(
    guid="9ec65e91-96a8-5cca-b61d-4d92742ab726",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Articuno.Name",
    display_name="Articuno",
    searchable_by=["Articuno", "Basic", "Articuno"],
    subtypes=["Basic"],
    collector_number=132,
    set_code="ME55",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=144,
    abilities=[
        Ability(
            title="Frosty Flapping",
            game_text="Once during your turn, if you have Moltres and Zapdos in play, you may use this Ability. Attach a Basic Water Energy card from your hand to this Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=all_legendary_birds_in_play_condition,
            effect=frosty_flapping,
        ),
        Attack(
            title="Hail",
            game_text="This attack does 30 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            effect=hail,
        ),
    ],
)