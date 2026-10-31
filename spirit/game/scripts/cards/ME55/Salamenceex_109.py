from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="38cbe18f-9c1d-5826-a724-0b2c593e6508",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salamenceex.Name",
    display_name="Salamence ex",
    searchable_by=["Salamence ex", "Stage 2", "ex", "Salamenceex"],
    subtypes=["Stage 2", "ex"],
    collector_number=109,
    set_code="ME55",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    family_id=373,
    abilities=[
        Attack(
            title="Booming Call",
            game_text="Put up to 3 Dragon Pok\u00e9mon from your discard pile onto your Bench.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top 2 cards of your deck.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1},
            damage=240,
            effect=unimplemented,
        ),
    ],
)